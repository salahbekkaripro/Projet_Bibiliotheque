from django.db import models 
from django import forms 
from django.contrib.auth.models import User


class Category(models.Model):
    name= models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Auteur(models.Model):
    name=models.CharField(max_length=120)
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class Livre(models.Model):
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    auteur=models.ForeignKey(Auteur,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField()
    lien=models.CharField(max_length=1000)


    def __str__(self) :
        return self.title




