from django.contrib import admin
from sqlapp.models import *

#adding tables to the database
admin.site.register(User)
admin.site.register(Poi)
