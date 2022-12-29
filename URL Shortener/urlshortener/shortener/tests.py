from django.test import TestCase
from .models import Url
from .views import redirect
from .utils import create_dummy_obj


class TestViews(TestCase):
    def test_url_dosent_exist(self):
        self.assertEqual(redirect('', "abc12").content.decode('utf-8'), "This url doesn't exist")

    def test_redirect(self):
        test_obj = create_dummy_obj()
        original_url = redirect('', test_obj.short_url).url
        new_counter = Url.objects.filter(short_url=test_obj.short_url).first().counter
        self.assertEqual(original_url, test_obj.original_url)  # checking valid long url.
        self.assertEqual(new_counter, 1)  # checking valid counter.

    def test_create(self):
        test_obj = create_dummy_obj()
        self.assertEqual(test_obj.counter, 0)
