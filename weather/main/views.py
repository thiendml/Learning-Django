from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):

    if request.method =="POST":
        city = request.POST['city']

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=87363a5d436a8d008951365f6d9e7400').read()

        list_of_data = json.loads(source)

        data = {
            "country_code " : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + 'k',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)

