from django.db import models
from datetime import datetime

class About(models.Model):
    title = models.CharField(max_length = 30000)
    name = models.CharField(max_length = 30000)
    photo_1 = models.ImageField(upload_to = 'about/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to = 'about/%Y/%m/%d/')
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.name

