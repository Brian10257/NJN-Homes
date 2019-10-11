from django.db import models
from datetime import datetime

class Consult(models.Model):
    name = models.CharField(max_length = 20000)
    email = models.EmailField(max_length = 2000)
    phone = models.CharField(max_length = 200, blank = True)
    subject = models.CharField(max_length = 500000, blank = True)
    message = models.TextField()
    contact_date = models.DateTimeField(default = datetime.now, blank =True)
    def __str__(self):
        return self.name