from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Articles(models.Model):
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username


class Comment(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

# Create your models here.
