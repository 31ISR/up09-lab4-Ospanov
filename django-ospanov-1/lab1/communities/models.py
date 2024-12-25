from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Community(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=True)
    avatar = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name