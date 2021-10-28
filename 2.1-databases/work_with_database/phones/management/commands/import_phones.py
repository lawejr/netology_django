import csv
from django.core.management.base import BaseCommand
from datetime import datetime
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.update_or_create(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=float(phone['price']),
                release_date=datetime.strptime(phone['release_date'], "%Y-%m-%d"),
                lte_exists=bool(phone['lte_exists'])
            )