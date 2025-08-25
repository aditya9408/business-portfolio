# portfolio/urls.py

from django.urls import path
from .views import home, all_projects, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('projects/', all_projects, name='all_projects'),
    path('contact/', contact_view, name='contact'),
]
