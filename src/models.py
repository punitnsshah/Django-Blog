from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):  #models.Model means inherit Model present in models package.
    title = models.CharField(max_length=60)  #CharField etc present in Model
    published_at = models.DateTimeField()
    description = models.TextField()
    #CharField is used to limit the amount of text. TextField can accept unlimited text.
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post)
    description = models.TextField()

    published_at = models.DateTimeField(default=timezone.now())

