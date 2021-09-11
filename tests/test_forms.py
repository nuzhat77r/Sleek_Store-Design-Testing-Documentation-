from django.test import DemoTestCase
from registrationform.views import *


class TestForms(DemoTestCase):

    def test_input_type_data(self):
        form = Edit_Post(data={
            'title': "test_username",
            'content': "test_id"
        })
        self.assertTrue(form.is_valid())

    def test_AddEditPostForm_form_no_data(self):
        form = Edit_Post(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)