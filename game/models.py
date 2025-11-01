from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Operator(models.Model):
    faction = models.CharField(max_length=100)
    skin = models.CharField(max_length=100)
    camo = models.CharField(max_length=100)
    unlock = models.TextField()
    image = models.ImageField(upload_to="game/", blank=True, null=True)
 

    def __str__(self):
        return self.skin 


class Weapon(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    characteristics = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="game/", blank=True, null=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Reply(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  



    def __str__(self):
        return self.content
    
