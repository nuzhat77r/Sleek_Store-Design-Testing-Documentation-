from unittest import TestCase

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.deletion import CASCADE




class RegisterConfirmTest(TestCase):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Email, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
       self.user(self.id)