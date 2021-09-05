from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

Division_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Chittagong','Chittagong'),
    ('Barishal','Barishal'),
    ('Sylhet','Sylhet'),
    ('Khulna','Khulna'),
    ('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),
)
class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality =models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 division = models.CharField(choices=Division_CHOICES, max_length =50)

 def __str__(self):
     return str(self.id)
