from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status, response
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from .models import *
from .serializers import *
import json
from rest_framework import status

class CoursesTest(APITestCase):

    def setUp(self):

        self.course_url = reverse('courses')
        User.objects.create(username='urmat111', password='123456')

    def test_courses_get(self):
        self.response = self.client.get(self.course_url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_courses_post(self):
        data = {
        "name": "Blasssbla",
        "description": "blabla",
        "logo": "img",
        "category": {
            "name": "Baling",
            "imgpath": "img"
        },
        "contacts": [
            {
                "status": 1
            }
        ],
        "branches": [
            {
                "latitude": "2131ssss2321",
                "longitude": "12321321",
                "address": "Osssssh"
            }
        ]
    }
        self.response = self.client.post(self.course_url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class CourseDetailTest(APITestCase):

    def setUp(self):

        self.category = Category.objects.create(name='test_category', imgpath='test_imgpath')
        self.branch = Branch.objects.create(latitude='1111111', longitude='2222222', address='Bishkek')
        self.contact = Contact.objects.create(status='1')
        self.course = Course.objects.create(
            name='test_course', description='test_description', logo='test_logo',
            category=self.category
        )
        self.url = reverse('course', kwargs={'course_id': self.course.id})




    def test_course_delete(self):

        self.response = self.client.delete(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_course_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


