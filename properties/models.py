from django.db import models
from datetime import datetime
from agents.models import Agent

class Property_single(models.Model):
    agent = models.ForeignKey(Agent, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length = 300)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits = 5, decimal_places = 1)
    garage = models.IntegerField(default = 0, blank = True) 
    area = models.CharField(max_length = 50000, blank = True)
    square  = models.IntegerField()
    amenity1 = models.CharField(max_length = 5000, blank = True)
    amenity2 = models.CharField(max_length = 5000, blank = True)
    amenity3 = models.CharField(max_length = 5000, blank = True)
    amenity4 = models.CharField(max_length = 5000, blank = True)
    amenity5 = models.CharField(max_length = 5000, blank = True)
    amenity6 = models.CharField(max_length = 5000, blank = True)
    amenity7 = models.CharField(max_length = 5000, blank = True)
    amenity8 = models.CharField(max_length = 5000, blank = True)
    amenity9 = models.CharField(max_length = 5000, blank = True) 
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

