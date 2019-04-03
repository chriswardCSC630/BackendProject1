from django.db import models
from django.conf import settings
from decimal import Decimal
import urllib
import json

# Used this as a model blueprint: https://djangobook.com/mdj2-models/
# Field parameters for User and Poi classes from https://docs.djangoproject.com/en/2.2/ref/models/fields/
class User(models.Model):
    userID = models.IntegerField(default=None)
    name = models.CharField(max_length = 60)
    username = models.CharField(max_length = 60)
    latitude = models.DecimalField(max_digits=18, decimal_places=10) #DecimalFields from https://docs.djangoproject.com/en/2.2/ref/models/fields/
    longitude = models.DecimalField(max_digits=18, decimal_places=10)

class Poi(models.Model):
    userID = models.IntegerField()
    poi_title = models.CharField(max_length = 60)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, editable=False)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, editable=False)

    def save(self):
        poi = "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip_code) #reverse geocoding needs street address in this format
        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(poi)
        super(Poi, self).save()

    #reverse geocoding documentation: https://developers.google.com/maps/documentation/geocoding/intro#ReverseGeocoding
    #example of reverse geocoding in python: https://andrewpwheeler.wordpress.com/2016/04/05/using-the-google-geocoding-api-with-python/
    def geocode(self, location):
        location = urllib.parse.quote_plus(location)
        print(location)
        request = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location, settings.GOOGLE_API_KEY)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read().decode('utf8'))

        if data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']

            return Decimal(lat), Decimal(lng)
