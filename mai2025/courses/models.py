from enum import Enum

from django.db import models

# Create your models here.

class Equipe(models.Model):
    code = models.CharField('code',max_length=3, unique=True)
    nom = models.CharField("nom",max_length=100)

    def __str__(self):
        return self.code

class Membre(models.Model):
    nom = models.CharField('nom',max_length=100)
    prenom = models.CharField('prenom',max_length=100)
    email = models.CharField('email',max_length=100,unique=True)
    appartient = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class EntraineurMembre(Membre):
    pass

class Coureur(Membre):
        dossard = models.IntegerField('dossard')
        entraineur = models.ForeignKey(EntraineurMembre, on_delete=models.CASCADE)

        def __str__(self):
            return f"Coureur {self.dossard}"

class Ville(models.Model):
    nom = models.CharField('nom',max_length=100)

class Etape(models.Model):
    date = models.DateField('date')
    depart = models.ForeignKey(Ville, related_name='etapes_depart', on_delete=models.CASCADE)
    arrive = models.ForeignKey(Ville, related_name='etapes_arrivee', on_delete=models.CASCADE)
    def __str__(self):
        return f"Étape du {self.date}"


class Sortie(Enum):
    Ab = 'Abandon'
    Ac = 'Accident'
    Di = 'Disqualification'

    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls]


class Court (models.Model):
    sortie = models.CharField(
        max_length=100,
        choices=Sortie.choices()
    )
    coureur = models.ForeignKey(Coureur,on_delete=models.CASCADE)
    etape = models.ForeignKey(Etape, on_delete=models.CASCADE)





