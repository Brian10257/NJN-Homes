from django.db import models
from datetime import datetime


class Service(models.Model):
    title= models.CharField(max_length = 5000, blank =True)
    slug = models.SlugField(max_length=200, unique=True)
    photo = models.ImageField(blank = True, upload_to = 'Services')
    description = models.TextField(blank = True)
    link = models.CharField(max_length = 5000, blank = True)
    upload_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title
