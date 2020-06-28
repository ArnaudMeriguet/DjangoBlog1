from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import post_list, cv_view

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,post_list)

class CvPageTest(TestCase):

    def test_cv_url_resolves_to_cv_page_view(self):
        found=resolve('/post/cv/')
        self.assertEqual(found.func,cv_view)

    def test_cv_page_returns_correct_html(self):
        request =HttpRequest()
        response= cv_view(request)
        html=response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Arnaud Meriguet</title>',html)
        self.assertTrue(html.endswith('</html>'))