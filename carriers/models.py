from django.db import models
from datetime import datetime
from django.urls import reverse

class Carrier(models.Model):
    logo = models.ImageField(blank = True, upload_to = 'Photos/Carrier/Company Logo/%Y/%m', null = True)
    company = models.CharField(max_length = 2000, blank = True)
    job_title = models.CharField(max_length = 2000, blank = True)
    slug = models.SlugField(max_length=200, unique=True)
    job_available = models.BooleanField(default = True, blank = True)
    address = models.CharField(max_length = 2000, blank = True)
    contact = models.CharField(max_length = 100, blank = True)
    website = models.CharField(max_length = 2000, blank = True)
    employer = models.CharField(max_length = 2000, blank = True)
    mail = models.CharField(max_length = 2000, blank  = True)
    date_posted = models.DateTimeField(default = datetime.now, blank = True)
    about_job = models.TextField(blank = True)
    salary = models.IntegerField(blank = True)
    experience = models.IntegerField(blank = True)
    is_published = models.BooleanField(default = True)
    responsibility_intro = models.TextField(blank =True)
    responsibility1 = models.CharField(max_length = 5000000, blank = True)
    responsibility2 = models.CharField(max_length = 5000000, blank = True)
    responsibility3 = models.CharField(max_length = 5000000, blank = True)
    responsibility4 = models.CharField(max_length = 5000000, blank = True)
    responsibility5 = models.CharField(max_length = 5000000, blank = True)
    responsibility6 = models.CharField(max_length = 5000000, blank = True)
    responsibility7 = models.CharField(max_length = 5000000, blank = True)
    responsibility8 = models.CharField(max_length = 5000000, blank = True)
    responsibility9 = models.CharField(max_length = 5000000, blank = True)
    responsibility10 = models.CharField(max_length = 5000000, blank = True)
    qualification_intro = models.TextField(blank = True)
    qualification1 = models.CharField(max_length = 5000000, blank = True)
    qualification2 = models.CharField(max_length = 5000000, blank = True)
    qualification3 = models.CharField(max_length = 5000000, blank = True)
    qualification4 = models.CharField(max_length = 5000000, blank = True)
    qualification5 = models.CharField(max_length = 5000000, blank = True)
    qualification6 = models.CharField(max_length = 5000000, blank = True)
    qualification7 = models.CharField(max_length = 5000000, blank = True)
    qualification8 = models.CharField(max_length = 5000000, blank = True)
    qualification9 = models.CharField(max_length = 5000000, blank = True)
    qualification10 = models.CharField(max_length = 5000000, blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    google_plus = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    linked_in = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('carrier', kwargs={'slug': self.slug})
    
class Apply(models.Model):
    docs = models.FileField(upload_to = 'Application Files/%Y/%m')
    name = models.CharField(max_length = 500000, blank = True)
    email = models.EmailField(max_length = 50000, blank = True)
    phone = models.CharField(max_length = 50000, blank = True)
    place_of_origin = models.CharField(max_length = 5000)
    current_city = models.CharField(max_length = 5000)
    neighbour_hood = models.CharField(max_length = 5000)
    current_employment = models.CharField(max_length = 50000)
    user_id = models.IntegerField()
    subject = models.CharField(max_length = 50000, blank = True)
    message = models.TextField(max_length = 50000, blank = True)
    application_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
