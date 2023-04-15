import random
import time
from django.core.management.base import BaseCommand
from core.models import Vehicle

class Command(BaseCommand):
    help = 'Simulate vehicle movement'

    def handle(self, *args, **options):
        # Define the range of latitude and longitude variation
        lat_lon_var = 0.1  # 0.1 degrees is approximately 11 km

        while True:
            print("Vehicle positions updating...")

            for vehicle in Vehicle.objects.all():
                vehicle.latitude = vehicle.latitude + random.uniform(-lat_lon_var, lat_lon_var)
                vehicle.longitude = vehicle.longitude + random.uniform(-lat_lon_var, lat_lon_var)
                vehicle.save()

            time.sleep(5)