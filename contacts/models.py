from django.db import models
from datetime import datetime
from properties.models import Property_single

class Contact(models.Model):
    property_single = models.CharField(max_length = 500)
    property_single_id = models.IntegerField()
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    message = models.TextField(blank = True) 
    contact_date = models.DateTimeField(default=datetime.now, blank = True)
    user_id = models.IntegerField(blank = True)
    def __str__(self):
        return self.name


