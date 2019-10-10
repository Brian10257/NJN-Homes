from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length = 50000, blank = True)
    sub_title = models.CharField(max_length = 50000, blank = True)
    photo = models.FileField(upload_to='photos/blog/%Y/%m', blank = True)
    author_name = models.CharField(max_length = 50000, blank = True)
    category = models.CharField(max_length = 50000, blank = True)
    introduction = models.TextField(blank = True)
    description1 = models.TextField(blank = True)
    description2 = models.TextField(blank = True)
    description3 = models.TextField(blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    pinterest = models.CharField(max_length = 50000, blank = True)
    image = models.ImageField(upload_to='photos/blog/comments/%Y', blank = True, null = True)
    user_name = models.CharField(max_length = 50000, blank = True)
    comment = models.TextField(blank = True)
    comment_date = models.DateTimeField(default = datetime.now, blank = True)
    date_published = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title