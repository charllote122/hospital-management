from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser programmatically'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@hospital.com',
                password='admin123456'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created: admin / admin123456'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Superuser already exists'))
