from django.db import models
from .category import Category




class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200 , default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


    @staticmethod
    def get_all_Categories_by_categoryId(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.get_all_procucts()



