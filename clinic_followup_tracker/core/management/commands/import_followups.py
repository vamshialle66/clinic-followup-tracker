import csv
from django.core.management.base import BaseCommand
from core.models import FollowUp, Clinic
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Import follow-ups from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('clinic_id', type=int)
        parser.add_argument('user_id', type=int)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        clinic = Clinic.objects.get(id=kwargs['clinic_id'])
        user = User.objects.get(id=kwargs['user_id'])

        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FollowUp.objects.create(
                    clinic=clinic,
                    created_by=user,
                    patient_name=row['patient_name'],
                    phone=row['phone'],
                    language=row.get('language', 'en'),
                    notes=row.get('notes', ''),
                    due_date=row['due_date']
                )

        self.stdout.write(self.style.SUCCESS('CSV import completed'))
