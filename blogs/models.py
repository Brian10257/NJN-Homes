from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length = 50000, blank = True)
    sub_title = models.CharField(max_length = 50000, blank = True)
    photo = models.FileField(upload_to='Photos/Blog/%Y/%m', blank = True)
    author_name = models.CharField(max_length = 50000, blank = True)
    category = models.CharField(max_length = 50000, blank = True)
    introduction = models.TextField(blank = True)
    description1 = models.TextField(blank = True)
    description2 = models.TextField(blank = True)
    description3 = models.TextField(blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    google_plus = models.CharField(max_length = 50000, blank = True)
    linkedin = models.CharField(max_length = 50000, blank = True)
    date_published = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    image = models.ImageField(upload_to='Photos/Blog_comments/%Y/%m',blank = True, null = True)
    name = models.CharField(max_length = 50000)
    email = models.EmailField(max_length = 5000, blank = True)
    website = models.CharField(max_length = 5000, blank = True)
    comment = models.TextField()
    comment_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.name