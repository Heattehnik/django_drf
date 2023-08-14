# Generated by Django 4.2.3 on 2023-08-14 09:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0018_alter_payment_datetime_alter_subscription_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 14, 9, 27, 36, 658227, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription",
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
