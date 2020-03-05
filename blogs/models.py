from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length = 50000, blank = True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_title = models.CharField(max_length = 50000, blank = True)
    photo = models.FileField(upload_to='Photos/Blog/%Y/%m', blank = True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.CharField(max_length = 50000, blank = True)
    content = models.TextField(blank = True)
    facebook = models.CharField(max_length = 50000, blank = True)
    twitter = models.CharField(max_length = 50000, blank = True)
    instagram = models.CharField(max_length = 50000, blank = True)
    google_plus = models.CharField(max_length = 50000, blank = True)
    linkedin = models.CharField(max_length = 50000, blank = True)
    status = models.IntegerField(choices=STATUS, default=1)
    date_published = models.DateTimeField(default = datetime.now, blank = True)
    
    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug':self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length = 50000)
    email = models.EmailField(max_length = 5000, blank = True)
    website = models.CharField(max_length = 5000, blank = True)
    body = models.TextField()
    active = models.BooleanField(default=True)
    comment_date = models.DateTimeField(default = datetime.now, blank = True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
