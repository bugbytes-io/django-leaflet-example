import random
import time
from django.core.management.base import BaseCommand
from core.models import Vehicle

class Command(BaseCommand):
    help = 'Simulate vehicle movement'

    def handle(self, *args, **options):
        # Define the range of latitude and longitude variation
        raise NotImplementedError