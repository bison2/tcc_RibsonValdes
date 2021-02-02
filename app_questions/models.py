from django.db import models
from django.urls import reverse

# Create your models here.

class GabManager(models.Manager):
    def all(self):
        qs=Gab.objects.all()

class Gab(models.Model):
    pergunta = models.CharField(max_length =100)
    resposta = models.CharField(max_length =100)
    gabarito= models.CharField(max_length = 20)

    
    def __str__(self):
        return self.gabarito

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug = self.slug)
       return reverse("questions:confere", kwargs={"gabarito": self.gabarito})