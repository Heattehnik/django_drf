# Generated by Django 4.2.3 on 2023-08-14 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_alter_payment_datetime_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 14, 6, 20, 43, 968041, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время",
            ),
        ),
    ]
