from django.contrib import admin
from django.urls import include, path
from django.views import View
from rest_framework import routers
from sqlapp.views import *

#set up all the urls for the server
urlpatterns = [
    path('', info.getUsers),
    path('admin/', info.getUsers),
    path('<str:user_id>/poi/', info.getPois, name="pois"),
    path('users/', info.getUsers, name="users"),
    path('users/<str:user_id>/', info.modifyUSR, name="modifyUSR"),
    path('locations/', info.getLocations, name="users"),
    path('locations/<str:user_id>/<str:title>/', info.modifyPOI, name="modifyPOI")
]
