from django.db import models
from autoslug import AutoSlugField
from category.models import Category

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    pub_date = models.DateField(auto_now_add=True, null=True)
    total_amount_products = models.IntegerField()
    sale = models.IntegerField(blank=True , null=True ,help_text='Leave Empty If Not Sale Product')
    image = models.FileField(max_length=100, upload_to="images/",null=True)
    new_slug = AutoSlugField(populate_from='title', null=True, default=True)
