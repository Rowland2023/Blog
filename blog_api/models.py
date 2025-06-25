from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author  = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete= models.CASCADE)
    content = models.TextField()
    author  = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)