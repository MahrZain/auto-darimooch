from django.db import models

# Create your models here.
class carousel(models.Model):
    title = models.CharField(max_length=60)
    caption = models.CharField(max_length=40)
    image = models.FileField(max_length=100 ,upload_to="carousel/", null=True )
