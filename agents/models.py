from django.db import models
from datetime import datetime

class Agent(models.Model):
    name = models.CharField(max_length = 30000, blank = True)
    role = models.CharField(max_length = 30000, blank = True)
    photo = models.ImageField(upload_to = 'photos/agents/%Y/%m', blank = True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length = 1000, blank = True)
    email = models.CharField(max_length = 5000, blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    pinterest = models.CharField(max_length = 50000, blank = True)
    dribbble = models.CharField(max_length = 50000, blank = True)
    is_mvp = models.BooleanField(default = False)
    hire_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.name

