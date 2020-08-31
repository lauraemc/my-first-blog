from django.test import TestCase
from django.urls import resolve
from blog.views import post_list, work_edit, edu_edit, skills_edit, extra_edit
from blog.forms import PostForm, WorkForm, EduForm, SkillsForm, ExtraForm

from django.http import HttpRequest 

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)

    #def test_home_page_returns_correct_html(self):
       #request = HttpRequest()  
        #response = post_list(request)  
        #html = response.content.decode('utf8').strip()

        #self.assertTrue(html.startswith('{% load static %}'))

        #self.assertIn('<title>Laura\'s Bridging Coursework!</title>', html)  
        #self.assertTrue(html.endswith('</html>'))

    def test_work_edit_url_resolves_to_work_edit_view(self):
        found = resolve('/work/1/edit/')  
        self.assertEqual(found.func, work_edit)

    def test_edu_edit_url_resolves_to_edu_edit_view(self):
        found = resolve('/education/1/edit/')  
        self.assertEqual(found.func, edu_edit)

    def test_skills_edit_url_resolves_to_skills_edit_view(self):
        found = resolve('/skills/1/edit/')  
        self.assertEqual(found.func, skills_edit)

    def test_extra_edit_url_resolves_to_extra_edit_view(self):
        found = resolve('/extra/1/edit/')  
        self.assertEqual(found.func, extra_edit)

    def test_work_valid_data(self):
        form = WorkForm(data={
            'dates': "2000-2001",
            'employer': "test employer",
            'location': "test location",
            'position': "test position",
            'assignments': "test assignment",
        })
        self.assertTrue(form.is_valid())
        work = form.save()
        self.assertEqual(work.dates, "2000-2001")
        self.assertEqual(work.employer, "test employer")
        self.assertEqual(work.location, "test location")
        self.assertEqual(work.position, "test position")
        self.assertEqual(work.assignments, "test assignment")




    def test_edu_valid_data(self):
        form = EduForm(data={
            'dates': "2000-2001",
            'title': "test title",
            'subTitle': "test subTitle",
            'text': "test text",
        })
        self.assertTrue(form.is_valid())
        school = form.save()
        self.assertEqual(school.dates, "2000-2001")
        self.assertEqual(school.title, "test title")
        self.assertEqual(school.subTitle, "test subTitle")
        self.assertEqual(school.text, "test text")

    def test_edu_valid_data(self):
        form = SkillsForm(data={
            'fluent': "test fluent",
            'experience': "test experience",
        })
        self.assertTrue(form.is_valid())
        school = form.save()
        self.assertEqual(school.fluent, "test fluent")
        self.assertEqual(school.experience, "test experience")


    def test_edu_valid_data(self):
        form = ExtraForm(data={
            'text': "test text",
        })
        self.assertTrue(form.is_valid())
        school = form.save()
        self.assertEqual(school.text, "test text")



    