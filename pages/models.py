from django.db import models
from datetime import datetime

class Services(models.Model): 
    manager_name = models.CharField(max_length = 50000, blank = True)
    phone = models.CharField(max_length = 50000, blank = True)
    service_1 = models.CharField(max_length = 500000, blank = True)
    description_1 = models.TextField(blank = True)
    service_2 = models.CharField(max_length = 500000, blank = True)
    description_2 = models.TextField(blank = True)
    service_3 = models.CharField(max_length = 500000, blank = True)
    description_3 = models.TextField(blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.service_1