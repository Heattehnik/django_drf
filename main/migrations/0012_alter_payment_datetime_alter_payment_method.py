# Generated by Django 4.2.3 on 2023-08-05 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_lesson_course_alter_payment_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 14, 15, 55, 867155, tzinfo=datetime.timezone.utc), verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('Безналичный', 'Безналичный'), ('Наличные', 'Наличные')], max_length=100, verbose_name='способ оплаты'),
        ),
    ]
