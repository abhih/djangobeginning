from time import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    index=models.AutoField(primary_key=True)
    topic=models.TextField(default='None',max_length=10,blank=False)
    text=models.TextField(max_length=180,blank=False,default='Blank post')
    created=models.DateTimeField(auto_now_add=True,editable=False)
    TYPES=(
        ('ML','Machine Learning'),
        ('DS','Data Science'),
            )
    tags=models.CharField(choices=TYPES,blank=False,default='None',max_length=100)

    def __str__(self):
        "to display the sting representation"
        return self.topic #text[:40]