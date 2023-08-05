from django.core.management import BaseCommand

from main.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        payment = Payment.objects.create(
            user_id='2',
            course_id='2',
            amount='5000',
            method='Нааличный'
        )

        payment.save()
