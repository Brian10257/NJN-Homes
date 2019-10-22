from django.db import models
from datetime import datetime

class Team(models.Model):
    photo1 = models.ImageField(blank = True, null =True)
    photo2 = models.ImageField(blank = True, null = True)
    name = models.CharField(max_length = 50000, blank =True)
    role = models.CharField(max_length= 500000, blank = True)
    date_posted = models.DateTimeField(default = datetime.now, blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    google_plus = models.CharField(max_length = 50000, blank = True)
    linkedin = models.CharField(max_length = 50000, blank = True)
    def __str__(self):
        return self.name