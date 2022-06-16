from django.db import models
from ckeditor.fields import RichTextField #เพิ่ม
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=200)
    descriptions=RichTextField()
    image=models.ImageField(upload_to='media/images')
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobOpportunities(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=200)
    email=models.EmailField(max_length = 254)
    link=models.URLField(max_length=200)
    descriptions=models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




