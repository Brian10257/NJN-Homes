from django.db import models
from datetime import datetime
from agents.models import Agent

class Property_single(models.Model):
    agent = models.ForeignKey(Agent, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length = 300,  blank = True)
    address = models.CharField(max_length = 300,  blank = True)
    city = models.CharField(max_length = 200,  blank = True)
    state = models.CharField(max_length = 200,  blank = True) 
    zipcode = models.CharField(max_length = 50,  blank = True)
    description1 = models.TextField(blank = True)
    description2 = models.TextField(blank = True)
    price = models.IntegerField()
    property_type = models.CharField(max_length = 5000, blank = True)
    status = models.CharField(max_length = 5000, blank = True) 
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits = 5, decimal_places = 1)
    garage = models.IntegerField() 
    area = models.CharField(max_length = 50000, blank = True)
    amenity1 = models.CharField(max_length = 5000, blank = True)
    amenity2 = models.CharField(max_length = 5000, blank = True)
    amenity3 = models.CharField(max_length = 5000, blank = True)
    amenity4 = models.CharField(max_length = 5000, blank = True)
    amenity5 = models.CharField(max_length = 5000, blank = True)
    amenity6 = models.CharField(max_length = 5000, blank = True)
    amenity7 = models.CharField(max_length = 5000, blank = True)
    amenity8 = models.CharField(max_length = 5000, blank = True)
    amenity9 = models.CharField(max_length = 5000, blank = True) 
    photo_main = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_1 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_2 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_3 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_4 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_5 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    photo_6 = models.ImageField(upload_to = 'Photos/Properties/%Y/%m', blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

