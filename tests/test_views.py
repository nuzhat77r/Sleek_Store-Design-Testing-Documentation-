import unittest
from django.test import SimpleTestCase
from cart.views import *


class TestForms(SimpleTestCase):

    def cart_list(self):
        form = ListForm(data={
            'title': "product_title",
            'qunatity': "product_quantity",
        })
        self.assertTrue(form.is_valid())

    def cart_list(self):
        form = ListForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
# Create your tests here.
