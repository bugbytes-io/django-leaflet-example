from django.http import JsonResponse
from django.shortcuts import render
from core.models import Vehicle

# Create your views here.
def index(request):
    context = {'vehicles': list(Vehicle.objects.values('latitude', 'longitude'))}
    return render(request, 'index.html', context)


def vehicle_positions(request):
    return JsonResponse(
        {'vehicles': list(Vehicle.objects.values('latitude', 'longitude'))}
    )