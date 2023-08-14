from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from main.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):
    def create_user(self):
        """User creation test"""
        self.new_user = User.objects.create(
            email='test@sky.pro',
            is_active=True,
        )
        self.new_user.set_password('test')
        self.new_user.save()

    def setUp(self) -> None:
        self.course = Course.objects.create(title='test')
        self.user = User.objects.create(email='test@example.com', password='test')
        self.data = {
            'course': self.course,
            'title': 'test',
            'owner': self.user
        }

        self.lesson = Lesson.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_lesson(self):
        """Lesson creation testing """
        data = {
            'course': self.course,
            'title': 'test2',
            'owner': self.user.pk
        }
        response = self.client.post('lessons/create/', data=data)
        print(response.__dict__)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)
    # def test_list_courses(self):
    #     """Test listing courses"""
    #     Course.objects.create(title="Test Course 1", description="This is a test course")
    #     response = self.client.get("/courses/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

