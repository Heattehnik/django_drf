from rest_framework import serializers

from main.models import Course, Lesson, Payment
from main.validators import TitleValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=('title',), queryset=Course.objects.all())
        ]

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=course)

        return course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True)
    lessons = LessonSerializer(many=True)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

