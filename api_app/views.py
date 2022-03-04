from django.shortcuts import render, redirect
# allows to interact with websites
import requests
import json

def renderData():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    print(response.json())
    return(data)





def index(request):
    context = {
        'data': renderData(),
    }
    return render(request, "index.html", context)