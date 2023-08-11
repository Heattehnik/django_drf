from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Course


class CourseTestCase(APITestCase):
    def setUp(self):
        pass

    def test_course_create(self):
        """Test creating a new course"""
        data = {
            "title": "Test Course",
            "description": "This is a test course",
            "lessons": [],
        }
        response = self.client.post("/courses/", data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["title"], data["title"])
        self.assertTrue(Course.objects.all().exists())
