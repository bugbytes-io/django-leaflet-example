import random
from django.core.management.base import BaseCommand
from core.models import Vehicle

class Command(BaseCommand):
    help = 'Generates vehicle objects in the database'

    def handle(self, *args, **options):
        NUM_VEHICLES_TO_GENERATE = 5
        for _ in range(NUM_VEHICLES_TO_GENERATE):
            Vehicle.objects.create(
                latitude=random.uniform(44,47),
                longitude=random.uniform(-100,-80)
            )

        print(f"{Vehicle.objects.count()} vehicles now in the database")