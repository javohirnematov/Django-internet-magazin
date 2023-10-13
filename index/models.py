from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_des = models.TextField(blank=True)
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='media')
    product_amount = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_count = models.IntegerField()

