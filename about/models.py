from django.db import models
from datetime import datetime

class About(models.Model):
    title = models.CharField(max_length = 30000)
    photo = models.ImageField(upload_to = 'Photos/About/%Y')
    description1 = models.TextField(blank=True)
    arreter = models.CharField(max_length = 50000, blank = True)
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    date_added = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

