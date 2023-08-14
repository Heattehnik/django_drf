# Generated by Django 4.2.3 on 2023-08-14 06:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0015_alter_payment_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 14, 6, 49, 3, 246330, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
