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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["title"], data["title"])
        self.assertTrue(Course.objects.all().exists())

    def test_list_courses(self):
        """Test listing courses"""
        Course.objects.create(title="Test Course 1", description="This is a test course")
        response = self.client.get("/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.json(), [{"title": "Test Course 1", "description": "This is a test course"}])