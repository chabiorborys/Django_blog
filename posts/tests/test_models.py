from django.test import TestCase
from posts.models import Video
from django.contrib.auth.models import User

class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='test1', email='test@gmail.com', password='123Test123')
        user.save()
        Video.objects.create(title="Test1",description='test_description1',path='FCJS2BBMGV18.02.2020.png',datetime='2021-01-07 17:53:15', user=user)

    def test_title_label(self):
        video = Video.objects.get(id=1)
        field_label = video._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        video = Video.objects.get(id=1)
        field_label = video._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_path_label(self):
        video = Video.objects.get(id=1)
        field_label = video._meta.get_field('path').verbose_name
        self.assertEqual(field_label, 'path')

    def test_datetime_label(self):
        video = Video.objects.get(id=1)
        field_label = video._meta.get_field('datetime').verbose_name
        self.assertEqual(field_label, 'datetime')

    def test_title_max_length(self):
        video = Video.objects.get(id=1)
        max_length = video._meta.get_field('title').max_length
        self.assertEqual(max_length, 30)
    
    def test_description_max_length(self):
        video = Video.objects.get(id=1)
        max_length = video._meta.get_field('description').max_length
        self.assertEqual(max_length, 300)

    def test_path_max_length(self):
        video = Video.objects.get(id=1)
        max_length = video._meta.get_field('path').max_length
        self.assertEqual(max_length, 60)