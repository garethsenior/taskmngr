from django.shortcuts import render
from .models import Chart


def index(request):
    charts = Chart.objects.all()
    return render(request, 'index.html', {
        'charts': charts
    })