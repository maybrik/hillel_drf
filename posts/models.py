from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=30)
    text = models.CharField(max_length=1400)
    image = models.URLField(max_length=200)


    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
