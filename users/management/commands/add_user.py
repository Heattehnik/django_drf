from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='user@sky.pro',
            phone='5555',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('user3')
        user.save()
