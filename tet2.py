##
import pyttsx3
import requests
from requests.exceptions import HTTPError
from googletrans import Translator

##
translator = Translator()
text = translator.translate('Hello, world!', dest='hi').text
##
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('rate', 170)
tts.setProperty('voice', voices[2].id)  #0 for male 1 for female

##
tts.say('Turn right, then immediately turn left onto Palm Beach Road')
tts.runAndWait()

##
base_url = "https://dev.virtualearth.net/REST/v1/Routes/Driving"
api_key = "Ak58g7T7bwYzFWk35yYqwNaeb6EbJAikga2SpRLbHept2oq4jz2YdLqKc2kTawpv"  # Replace with your actual API key
origin = "Vashi Railway Station"
destination = "Koparkhairne Railway Station"

url = f"{base_url}?wp.0={origin}&wp.1={destination}&key={api_key}"

##
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for error responses
except HTTPError as e:
    print(e)
finally:
    data = response.json()
##
print(data['resourceSets'][0]['resources'][0]['travelDistance'])
print(data['resourceSets'][0]['resources'][0]['travelDuration'])

for way in data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems']:
    print(way['instruction']['text'])
    print(way['maneuverPoint']['coordinates'])
    print(way['travelDistance'],'KM')
    print(way['travelDuration']/60,'s\n')