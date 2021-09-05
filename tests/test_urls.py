import unittest
from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import *


class UrlsTest(TestCase):

    def add_to_cart_is_resolved(self):
        url = reverse('add-to-cart', args=[1])
        self.assertEquals(resolve(url).func, add_to_cart_view)

    def show_to_cart_is_resolved(self):
        url = reverse('show-cart', args=[1])
        self.assertEquals(resolve(url).func, show_to_cart_view)

    def plus_cart_is_resolved(self):
        url = reverse('plus-cart', args=[1])
        self.assertEquals(resolve(url).func, plus_cart_view)

    def minus_cart_is_resolved(self):
        url = reverse('minus-cart', args=[1])
        self.assertEquals(resolve(url).func, minus_cart_view)

    def remove_cart_is_resolved(self):
        url = reverse('remove-cart', args=[1])
        self.assertEquals(resolve(url).func, remove_cart_view)