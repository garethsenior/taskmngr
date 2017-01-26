import requests
import json

from .models import Chart

def get_chart_data():
    uri = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topsongs/sf=143444/limit=1/explicit=true/json"
    resp = requests.get(uri)
    data = json.loads(resp.text)
    try:
        number1 = data['feed']['entry']['title']['label']
    except KeyError:
        number1 = 'Unknown'
    chart = Chart.objects.create(data=resp.text, number1=number1)
    print("Imported Chart ID: {}".format(chart.id))