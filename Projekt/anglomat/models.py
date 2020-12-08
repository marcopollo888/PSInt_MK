from django.db import models

# Create your models here.

class Verb(models.Model):
    infinitive = models.CharField(max_length=200)
    past_tense = models.CharField(max_length=200)
    past_participle = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)

class Numeral(models.Model):
    cardinal_number = models.CharField(max_length=200)
    ordinal_number = models.CharField(max_length=200)

#class Results(models.Model)
    #score = models.IntegerField()
