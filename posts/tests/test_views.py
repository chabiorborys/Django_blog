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

class ContactPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contact/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

class RegisterPageViewTest(TestCase):
    @classmethod
    def setUp(self):
        self.register_url=reverse('register')
        self.user={
            'username':'username',
            'password':'password',
            're_password':'password',
            'first_name':'first_name',
            'last_name':'last_name',
            'email':'email@gmail.com'
        }
      
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_user_can_register(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

class LoginPageViewTest(TestCase):
    @classmethod
    def setUp(self):
        self.login_url=reverse('login')
        self.register_url=reverse('register')
        self.user={
            'username':'username',
            'password':'password',
            're_password':'password',
            'first_name':'first_name',
            'last_name':'last_name',
            'email':'email@gmail.com'
        }
    
    def test_view_exists_at_desired_loction(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_can_login(self):
        self.client.post(self.register_url,self.user,format='text/html')
        user = User.objects.filter(email=self.user['email']).first()
        #Activate user, otherwise he won't be able to log in
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

    def test_cant_login_with_no_username(self):
        response = self.client.post(self.login_url,{'username':'','password':'password'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_cant_login_with_no_password(self):
        response = self.client.post(self.login_url,{'username':'username','password':''}, format='text/html')
        self.assertEqual(response.status_code, 401)