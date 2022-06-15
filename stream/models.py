from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    image = models.ImageField(null=False, blank=False)
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=100)
    mtumiaji = models.ForeignKey(User, on_delete=models.CASCADE)
    timed_created = models.DateTimeField(auto_now_add=True)
    # avoid adding comments field so as to be able to link it to the user logged in
    likes = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return str(self.image_name)

    def __str__(self) -> str:
        return str(self.image_caption)

    def __str__(self) -> str:
        return str(self.mtumiaji)

    def __str__(self) -> str:
        return str(self.timed_created)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Comment(models.Model):
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    mtumiaji = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body

    def __str__(self) -> str:
        return self.time_created

    def __str__(self) -> str:
        return self.post

    def __str__(self) -> str:
        return self.mtumiaji


class Profile(models.Model):
    photo = models.ImageField(null=False, blank=False)
    bio = models.TextField(default='Bio', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'


class NewPost(models.Model):
    image = models.ImageField(null=False, blank=False)
