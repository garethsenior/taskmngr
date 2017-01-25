import requests
import json

from .models import Chart

def get_chart_data():
    uri = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topsongs/sf=143444/limit=1/explicit=true/json"
    resp = requests.get(uri)
    data = json.loads(resp.text)
    chart = Chart.objects.create(data=resp.text, number1=data['feed']['entry']['title']['label'])
    print("Imported Chart ID: {}".format(chart.id))