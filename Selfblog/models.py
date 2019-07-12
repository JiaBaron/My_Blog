from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title=models.CharField(max_length=32)

    time=models.DateField(auto_now=True)
    description=RichTextField()
    content=RichTextField()
    image=models.ImageField(upload_to='images')
    types=models.ForeignKey(to='Types',on_delete=True)
    author = models.ForeignKey(to='Author',on_delete=True)
    read_num=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Types(models.Model):
    types=models.CharField(max_length=32)
    def __str__(self):
        return self.types

class Author(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Message(models.Model):
     name=models.CharField(max_length=32)
     time=models.DateTimeField(auto_now=True)
     photo=models.ImageField(upload_to='images',default='/static/images/1.jpg')
     message=models.TextField()

     def __str__(self):
         return self.name

class Pictures(models.Model):
    picture=models.ImageField(upload_to='images')

class Touch(models.Model):
    name=models.CharField(max_length=32)
    gender=models.CharField(max_length=32)
    phone=models.CharField(max_length=32)
    def __str__(self):
        return self.name



# Create your models here.
