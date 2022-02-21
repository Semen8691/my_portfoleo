from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()



class Field(models.Model):
    number = models.IntegerField()




class Human(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now=True)




class YouTube(models.Model):
    date = models.DateTimeField(auto_now=True)
    searth = models.CharField(max_length=40)
    online = models.IntegerField()


class Russia(models.Model):
    date = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    main = models.CharField(max_length=20)
