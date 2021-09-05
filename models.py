from django.db import models
from django.db.models.deletion import CASCADE

CATEGORY_CHOICES = (
 ('W', 'Women'),
 ('M', 'Men'),
 ('J', 'Jewellery'),
 ('H', 'Home Decor'),
)
class Product(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.
    this class used to create objects for database entry

    """
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
    Product_image =models.ImageField(upload_to='productming')

    def __str__(self):
       return str(self.id)