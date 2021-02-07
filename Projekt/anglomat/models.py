from django.db import models

class Klient(models.Model):
    PESEL = models.CharField(max_length=11, primary_key=True, unique=True)
    Imie = models.CharField(max_length=40)
    Nazwisko = models.CharField(max_length=40)
    Telefon = models.CharField(max_length=12)

    class Meta:
        ordering = ('Nazwisko',)

    def __str__(self):
        return self.Imie+' '+self.Nazwisko


class Auto(models.Model):
    NrRejestracyjny = models.CharField(max_length=8, primary_key = True, unique=True)
    Marka = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    VIN = models.CharField(max_length=15, unique=True)
    DataPierwszejRejestracji = models.DateField()

class Naprawa(models.Model):
 IdKlienta = models.ForeignKey(Klient, on_delete=models.CASCADE, db_column='PESEL')
 IdAuta = models.ForeignKey(Auto, on_delete=models.CASCADE, db_column='NrRejestracyjny')
 Cena = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False)
 DataZlecenia = models.DateField()

