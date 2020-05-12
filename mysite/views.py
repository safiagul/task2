import requests

from django.http import HttpResponse
from django.shortcuts import render

from ipware import get_client_ip


def index(request):
  ip_address_value = get_client_ip(request)[0]
  response = requests.get("http://ip-api.com/json/{}".format(ip_address_value))
  data = dict(response.json())
  
  return render(request, 'index.html', context = data)