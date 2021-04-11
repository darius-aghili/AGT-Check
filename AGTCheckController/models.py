from django.db import models

class FahrzeugTyp(models.Model):
    name = models.CharField(max_length=10)

class Verwaltung(models.Model):
    name = models.CharField(max_length=5)
  
class Organisation(models.Model):
    name = models.CharField(max_length=10)

class Einheit(models.Model):
    nummer = models.IntegerField()
    name = models.CharField(max_length=30)

class Fahrzeug(models.Model):
    opta1 = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    opta2 = models.ForeignKey(Verwaltung, on_delete=models.CASCADE)
    opta3 = models.ForeignKey(Einheit, on_delete=models.CASCADE)
    opta4 = models.ForeignKey(FahrzeugTyp, on_delete=models.CASCADE)

class PAStandort(models.Model):
    fahrzeugID = models.ForeignKey(Fahrzeug, on_delete=models.CASCADE)
    standort = models.CharField(max_length=10)

class Pruefer(models.Model):
    name = models.CharField(max_length=25)
    vorname = models.CharField(max_length=25)

class TotmannwarnerStatus(models.Model):
    status = models.CharField(max_length=15)

class AGTHolsterStatus(models.Model):
    status = models.CharField(max_length=15)

class AGTPlaketteStatus(models.Model):
    status = models.CharField(max_length=15)

class Pruefung(models.Model):
    prueferID = models.ForeignKey(Pruefer, on_delete=models.CASCADE)
    paStandortID = models.ForeignKey(PAStandort, on_delete=models.CASCADE)
    totmannwarnerStatusID = models.ForeignKey(TotmannwarnerStatus, on_delete=models.CASCADE)
    agtHolsterStatusID = models.ForeignKey(AGTHolsterStatus, on_delete=models.CASCADE)
    agtPlaketteStatusID = models.ForeignKey(AGTPlaketteStatus, on_delete=models.CASCADE)
    paNummer = models.IntegerField()
    druck = models.IntegerField()
    druckabfall = models.IntegerField()
    restdruckwarneinrichtung = models.BooleanField()
    flammschutzhaube = models.BooleanField()
    pruefungOK = models.BooleanField()
    datum = models.DateTimeField(auto_now=True)
