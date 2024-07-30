from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=60)
    image = models.FileField(max_length=100, upload_to="category/",null=True)