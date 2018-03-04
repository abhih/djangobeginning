from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Blogger(models.Model):
    title=models.CharField(max_length=180)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_details_view', args=[str(self.id)])