from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.models import Skill
from blog.views import post_list, cv_view

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'blog/post_list.html')

class CvPageTest(TestCase):

    def test_cv_page_uses_cv_template(self):
        response= self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv_view.html')

    def test_can_save_a_POST_request(self):
        response=self.client.post('/cv/',data={'skill_text':'A new skill in list'})
        self.assertIn('A new skill in list', response.content.decode())
        self.assertTemplateUsed(response,'blog/cv_view.html')

class SkillModelTest(TestCase):

    def test_saving_and_retrieving_skills(self):
        firstSkill=Skill()
        firstSkill.text="The first list skill"
        firstSkill.save()
        
        secondSkill=Skill()
        secondSkill.text="Second skill of the list"
        secondSkill.save()
        
        savedSkills=Skill.objects.all()
        self.assertEqual(savedSkills.count(),2)

        firstSavedSkill=savedSkills[0]
        secondSavedSkill=savedSkills[1]
        self.assertEqual(firstSavedSkill.text,"The first list skill")
        self.assertEqual(secondSavedSkill.text,"Second skill of the list")