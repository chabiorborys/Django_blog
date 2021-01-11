from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

class LandingPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test1', email='test@gmail.com', password='123Test123')
        user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class BlogPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tech/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/tech/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tech.html')

class AboutPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class ContactPageView(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contact/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')