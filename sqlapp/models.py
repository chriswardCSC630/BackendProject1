from django.db import models

# used this as a model blueprint: https://djangobook.com/mdj2-models/
class User(models.Model):
     name = models.CharField(max_length = 60)
     username = models.CharField(max_length = 60)
     longitude = models.FloatField() # FloatField command https://stackoverflow.com/questions/36515661/django-models-number-field
     latitude = models.FloatField()
