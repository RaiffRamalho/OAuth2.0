import httplib2
import json


def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyCdoyrmoiyigL2AO60Qrrk3FAxPl4Y3Xr4"
    locationString = inputString.replace(" ", "+")
    print(locationString)
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    print(url)
    h = httplib2.Http()
    req = h.request(url,'GET')[1]
    result = json.loads(req)
    print(result)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)