import unittest
from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import *


class UrlsTest(TestCase):

    def test_community_home_view_url_is_resolved(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, success) 