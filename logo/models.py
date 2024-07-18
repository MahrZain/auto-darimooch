from django.db import models

# Create your models here.
class limage(models.Model):
    image = models.FileField(upload_to="logo/",null=True,blank=True, help_text="Logo Must Be Only One Image")