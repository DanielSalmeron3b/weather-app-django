from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=d0993b32cf3e8409052fec7c281fa054').read()
        # Converting the JSON data to a dictionary
        # The 'list_of_data' will hold everythin that we are requesting
        list_of_data = json.loads(source)
        # The 'data' variable will hold everything that will be rendered on the HTML
        # The values and keys are provided by the API, you can see them on api.openweathermap.org/current
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ,' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            # 'weather' contains a list of data. So we are choosing the first index which is [0]
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)


