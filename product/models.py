from django.db import models
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    price = models.CharField(max_length=100, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    delete = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ['-data']

    def get_absolute_url(self):
        return reverse('home:index_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title


class ImageProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=False)
    othersphoto = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.product.title
