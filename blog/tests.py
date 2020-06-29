from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import post_list, cv_view

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'blog/post_list.html')

class CvPageTest(TestCase):

    def test_cv_page_uses_cv_template(self):
        response= self.client.get('/post/cv/')
        self.assertTemplateUsed(response, 'blog/cv_view.html')

    def test_can_save_a_POST_request(self):
        response=self.client.post('/post/cv/',data={'skill_text':'A new skill in list'})
        self.assertIn('A new skill in list', response.content.decode())
        self.assertTemplateUsed(response,'blog/cv_view.html')
