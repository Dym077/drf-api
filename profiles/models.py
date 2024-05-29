from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../https://res-console.cloudinary.com/dx5y0mmme/thumbnails/v1/image/upload/v1715679145/bWVkaWEvaW1hZ2VzL2RlZmF1bHRfcHJvZmlsZV9yZWx4b3M=/drilldown'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)        
