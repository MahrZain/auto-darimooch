from django.db import models
from autoslug import AutoSlugField
from category.models import Category

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    price = models.IntegerField()
    pub_date = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(max_length=60)
    total_amount_products = models.IntegerField()
    sale = models.IntegerField(blank=True , null=True ,help_text='Leave Empty If Not Sale Product')
    image = models.FileField(max_length=100, upload_to="images/",null=True)
    new_slug = AutoSlugField(populate_from='title', null=True, default=True)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)