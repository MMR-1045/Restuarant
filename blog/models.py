from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog/',blank=True,null=True)
    
    #tags
    category=models.ForeignKey('Category', null=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(default=timezone.now)
    
    tags = TaggableManager(blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'


class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    contend=models.TextField()
    created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.contend)