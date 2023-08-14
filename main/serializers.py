from rest_framework import serializers

from main.models import Course, Lesson, Payment, Subscription
from main.validators import TitleValidator, URLValidator
from users.serializers import SubscriptionSerializer


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
        course = Course.objects.create(owner=self.context['request'].user, **validated_data)
        return course


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    lessons_count = serializers.IntegerField(source="lessons.count", read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    def get_is_subscribed(self, instance):
        request = self.context['request']
        subscription = Subscription.objects.filter(user=request.user,
                                                   course=instance)
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
