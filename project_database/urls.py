from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import routers
from sqlapp.models import *

class displayPois(View):

    def getPois(requets, usr):
        data = {}
        id = User.objects.get(username=usr).id
        for place in Poi.objects.filter(userID=id):
            data[place.poi_title] = (float(place.latitude), float(place.longitude))
        return JsonResponse(data)

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('<str:usr>/poi', displayPois.getPois, name="pois"),
]
