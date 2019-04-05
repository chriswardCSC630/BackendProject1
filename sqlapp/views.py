from sqlapp.models import *
from django.views import View
from django.http import JsonResponse, QueryDict, HttpResponse

# Handles all requests from urls.py
class info(View):

    def instructions(request):
        return HttpResponse("<a>https://raw.githubusercontent.com/chriswardCSC630/BackendProject1/master/instructions.txt<a>")

    #handle GET and POST requests at server/user_id/poi
    def getPois(request, user_id):
        if request.method == "GET":
            data = {}
            for place in Poi.objects.filter(userID=user_id):
                data[place.poi_title] = (float(place.latitude), float(place.longitude))
            return JsonResponse(data)
        elif request.method == "POST":
            data = QueryDict(request.META["QUERY_STRING"]).dict()
            Poi.objects.create(userID=data["userID"], poi_title=data["poi_title"], address=data["address"], city=data["city"], state=data["state"], zip_code=data["zip_code"])
            return JsonResponse({"message": "POSTed"})

    #handle GET and POST requests at server/users/
    def getUsers(request):
        if request.method == "GET":
            data = {}
            for usr in User.objects.all():
                data[usr.userID] = "Name: " + str(usr.name) + ": Username: " + str(usr.username)
            return JsonResponse(data)
        elif request.method == "POST":
            data = QueryDict(request.META["QUERY_STRING"]).dict()
            User.objects.create(userID=data["userID"], name=data["name"], username=data["username"], latitude=data["latitude"], longitude=data["longitude"])
            return JsonResponse({"message": "POSTed"})

    #return a formatted version of all users' homebases and places of interest at server/locations/
    def getLocations(requets):
        data = {}
        for usr in User.objects.all():
            pois = ""
            for place in Poi.objects.filter(userID=usr.userID):
                pois += "(" + place.poi_title + ": " + str(place.latitude) + ", " + str(place.longitude) + ")"
            data[usr.userID] = "Homebase: " + str(usr.latitude) + ", " + str(usr.longitude) + " | Points of Interest: {" + pois + "}"
        return JsonResponse(data)

    #handles POST and DELETE from server/users/user_id
    def modifyUSR(request, user_id):
        return info.modify(request, User.objects.get(userID=user_id))

    #handles POST and DELETE from server/locations/user_id/poi_title
    def modifyPOI(request, user_id, title):
        return info.modify(request, Poi.objects.get(userID=user_id, poi_title=title))

    #modify function to handle modifying users and places of interest
    def modify(request, object):
        if request.method == "PATCH":
            data = QueryDict(request.META["QUERY_STRING"]).dict()
            #loop from https://stackoverflow.com/questions/1576664/how-to-update-multiple-fields-of-a-django-model-instance
            for (key, value) in data.items():
                setattr(object, key, value)
            object.save() #save the modified object
            return JsonResponse({"message": "PATCHed"})
        if request.method == "DELETE":
            object.delete()
            return JsonResponse({"message": "DELETEd"})
