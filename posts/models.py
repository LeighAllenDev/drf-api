from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    Post model, relating to owner, the user isntance. 
    default image set to always reference image.url
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_nwigev',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return f'{self.id} {self.title}'