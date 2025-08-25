from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('bedroom', 'Bedroom'),
        ('hall', 'Hall'),
        ('kitchen','Kitchen'),
        ('tvunit', 'TvUnit'),
        ('sofa', 'Sofa'),
        ('centertable','CenterTable'),
        ('bed','Bed'),
        ('cupboard','CupBoard'),
        ('door','Door'),
        ('others','Others')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name