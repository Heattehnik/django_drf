from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='обложка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='обложка', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео')
