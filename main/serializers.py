from rest_framework import serializers

from main.models import Course, Lesson, Payment
from main.validators import TitleValidator, URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            URLValidator(field="video_url"),
            serializers.UniqueTogetherValidator(
                fields=("video_url",), queryset=Lesson.objects.all()
            ),
        ]


class CourseCreateSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        validators = [
            TitleValidator(field="title"),
            serializers.UniqueTogetherValidator(
                fields=("title",), queryset=Course.objects.all()
            ),
        ]

    def create(self, validated_data):
        lessons = validated_data.pop("lessons")
        course = Course.objects.create(**validated_data)

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=course)

        return course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    lessons_count = serializers.IntegerField(source="lessons.count", read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
