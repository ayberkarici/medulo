from django.core.management.base import BaseCommand
from core.models import create_sample_data

class Command(BaseCommand):
    help = 'Populate the database with sample Medula Eczane data.'

    def handle(self, *args, **kwargs):
        create_sample_data()
        self.stdout.write(self.style.SUCCESS('Sample data populated successfully.'))
