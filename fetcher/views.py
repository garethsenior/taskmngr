from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Chart
from .tasks import delayed_get_chart_data

def index(request):
    charts = Chart.objects.all()
    return render(request, 'index.html', {
        'charts': charts
    })

def create(request):
    # delay this for 10seconds
    delayed_get_chart_data.delay(5)
    return HttpResponseRedirect('/')