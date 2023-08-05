from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='обложка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='обложка', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE,
                               related_name='lessons')


class Payment(models.Model):

    CARD = 'безналичный'
    CASH = 'наличный'

    PAYMENT_METHOD = [
        (CARD, 'Безналичный'),
        (CASH, 'Наличные'),
    ]

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name='пользователь')
    datetime = models.DateTimeField(default=timezone.now(), verbose_name='Дата и время')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1, verbose_name='курс')
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма')
    method = models.CharField(max_length=100, choices=PAYMENT_METHOD, verbose_name='способ оплаты')
