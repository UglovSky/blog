from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, name = 'title')
    content = models.TextField(name = 'content')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
