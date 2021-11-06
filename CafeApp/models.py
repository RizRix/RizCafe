from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=250, unique=True)
    cslug = models.SlugField(max_length=250, unique=True)
    cdes = models.TextField()
    cimg = models.ImageField(upload_to='picture')

    class Meta:
        ordering = ('cname',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.cname

    def get_url(self):
        return reverse('pro_menu', args=[self.cslug])


class Products(models.Model):
    pname = models.CharField(max_length=250, unique=True)
    pslug = models.SlugField(max_length=250, unique=True)
    pcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    pprice = models.FloatField()
    pimg = models.ImageField(upload_to='picture')
    pdes = models.TextField()
    pstock = models.IntegerField()
    pavailable = models.BooleanField()

    def __str__(self):
        return self.pname

    def get_url(self):
        return reverse('Display', args=[self.pcategory.cslug, self.pslug])
