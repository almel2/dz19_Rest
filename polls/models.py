from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_create = models.DateField(auto_now_add=True)

    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    message = models.TextField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{" ".join(self.message.split()[:3])}'