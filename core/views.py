from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    all_projects = Project.objects.order_by("id")      # Remove randomness
    displayed_projects = all_projects[:6]              # Load up to 6 projects

    show_thankyou = request.session.pop("show_thankyou", False)

    return render(
        request,
        "portfolio/home.html",
        {
            "projects": displayed_projects,
            "total_projects_count": all_projects.count(),
            "show_thankyou": show_thankyou,
        }
    )
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            subject = f"New Contact Message from {contact_message.name}"
            message = f"""Name: {contact_message.name}
Phone: {contact_message.phone}
Message:
{contact_message.message}"""
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL]
            )

            request.session["show_thankyou"] = True
            return redirect('home')
    return redirect('home')
def all_projects(request):
    selected_category = request.GET.get("category")
    page_number = request.GET.get("page", 1)

    if selected_category and selected_category != "all":
        projects = Project.objects.filter(category=selected_category).order_by('-id')
    else:
        projects = Project.objects.all().order_by('-id')

    paginator = Paginator(projects, 8)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string("portfolio/includes/project_cards.html", {
            "projects": page_obj,
        })
        return JsonResponse({
            "html": html,
            "has_next": page_obj.has_next()
        })

    categories = Project.objects.values_list('category', flat=True).distinct()

    return render(request, "portfolio/all_projects.html", {
        "projects": page_obj,
        "categories": categories,
        "selected_category": selected_category,
    })
