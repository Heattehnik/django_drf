# Generated by Django 4.2.3 on 2023-08-14 09:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_alter_payment_datetime_alter_subscription_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 14, 9, 5, 3, 246756, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription",
                to="main.course",
                verbose_name="курс",
            ),
        ),
    ]
