from django.db import models
from django.urls import reverse

# Create your models here.

class GabManager(models.Manager):
    def all(self):
        qs=Gab.objects.all()




class Gab(models.Model):
    CPF=1
    RG=2
    CNH=3

    TIPO_CHOICES=(
        (CPF,'1-CPF'),
        (RG,'2-RG'),
        (CNH,'3-CNH'),
    )

    CPF='CPF'
    RG='RG'
    CNH='CNH'

    TIPO_CHOICESII=(
        (CPF,'CPF'),
        (RG,'RG'),
        (CNH,'CNH'),
    )
    alternativa = models.IntegerField(choices=TIPO_CHOICES, default=1)
    alternativa2 = models.CharField(max_length=20,choices=TIPO_CHOICESII, default='RG')
    pergunta = models.CharField(max_length =100)
    resposta = models.CharField(max_length =100)
    gabarito= models.CharField(max_length = 20)
   

    def __str__(self):
        return self.gabarito

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug = self.slug)
       return reverse("questions:resposta", kwargs={"id": self.id})