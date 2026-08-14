from django.core.management.base import BaseCommand
from apps.analytics.models import Analytics
from django.utils import timezone

class Command(BaseCommand):
    help = 'Load sample analytics data'

    def handle(self, *args, **options):
        data = [
            ('patient', 'Total Patients', 150, 'All', 'August 2026'),
            ('appointment', 'Monthly Appointments', 245, 'All', 'August 2026'),
            ('revenue', 'Monthly Revenue', 45000, 'All', 'August 2026'),
            ('pharmacy', 'Pharmacy Sales', 12000, 'Pharmacy', 'August 2026'),
            ('satisfaction', 'Patient Satisfaction', 4.5, 'All', 'August 2026'),
            ('wait_time', 'Average Wait Time', 15, 'All', 'August 2026'),
            ('turnover', 'Patient Turnover', 85, 'All', 'August 2026'),
        ]

        for metric_type, title, value, department, period in data:
            Analytics.objects.create(
                metric_type=metric_type,
                title=title,
                value=value,
                description=f'{title} for {period}',
                time_period=period,
                department=department,
                previous_value=0,
                change_percentage=0,
                date=timezone.now().date()
            )
            self.stdout.write(f'✅ Created: {title}')

        self.stdout.write(self.style.SUCCESS('🎉 All analytics data loaded!'))
