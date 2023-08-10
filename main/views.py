from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from main.models import Course, Lesson, Payment
from main.permissions import IsOwner, IsNotStuff, IsStuff
from main.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, CourseCreateSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(owner=self.request.user)


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = [IsNotStuff]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwner, IsStuff]


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsOwner]


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsNotStuff]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStuff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('method', 'course',)
    search_fields = ['course', 'method']
    ordering_fields = ['datetime']


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
