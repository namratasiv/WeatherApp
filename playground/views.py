from django.shortcuts import render
from django.http import HttpResponse
import json, ssl
import urllib.request
from playground.models import Weather

# Create your views here.
def say_hello(request):
    if request.method == 'POST':
        city = request.POST['city']
        context = ssl._create_unverified_context() 
        source = urllib.request.urlopen(
        "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=19a53fd07f86cf28ac16b4ce0f9398de&units=metric",context=context
        ).read()
        listofdata = json.loads(source)
    
        data = {
            "temp": str(listofdata['main']['temp']) + ' °C',
            "city":str(city)
        }
        
        #p.save()
        w = Weather.objects
        p = Weather.objects.get_or_create(city=city,temp=data['temp'])
        if p:
            print(data)
    else:
        return render(request,'index.html')
    return render(request,'index.html',{'w':w})
