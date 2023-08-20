from django.db import models

class Niveau(models.Model):
    nom = models.CharField(max_length=50)
   # groupes = models.ManyToManyField('Groupe', related_name='niveaux')
    class Meta:
        verbose_name="Niveau"
    def __str__(self):
        return self.nom
'''
class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    groupes = models.ManyToManyField('Groupe', related_name='matieres')
'''


    
class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    niveaux = models.ManyToManyField(Niveau, related_name='matieres')
    
class Grade(models.Model):
    nom = models.CharField(max_length=50)
    heure= models.IntegerField(blank=True, null=True)# nombre d'eure par semaine en fonction de la grade 
    status=models.BooleanField(blank=True, null=True)#disponible ou pas 
    def __str__(self):
        return self.nom

class Professeur(models.Model):
    matricule=models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom=models.TextField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    cycle = models.ForeignKey('Cycle', on_delete=models.CASCADE)
    matieres = models.ManyToManyField(Matiere, related_name='professeurs')

class Cycle(models.Model):
    libelle = models.CharField(max_length=50)
    professeurs = models.ManyToManyField(Professeur, related_name='cycles')

class Salle(models.Model):
    libelle = models.CharField(max_length=50)
    batiment = models.ForeignKey('Batiment', on_delete=models.CASCADE)
    class Meta:
        verbose_name="Salle"
        
    def __str__(self):
        return self.libelle

class Batiment(models.Model):
    libelle = models.CharField(max_length=50)
    class Meta:
        verbose_name="Batiment"
    def __str__(self):
        return self.libelle

class Duree(models.Model):
    libelle = models.CharField(max_length=20)
    matieres = models.ManyToManyField(Matiere, related_name='durees')
    niveaux = models.ManyToManyField(Niveau, related_name='durees')
    class Meta:
        verbose_name="Durée"

class Jours(models.Model):
    libelle = models.CharField(max_length=20)
    class Meta:
        verbose_name="Jour"
    def __str__(self):
        return self.libelle

class Heure(models.Model):
    libelle = models.CharField(max_length=20)
    class Meta:
        verbose_name="Heure"
    def __str__(self):
        return self.libelle

class Cours(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE)
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    jours = models.ForeignKey(Jours, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    class Meta:
        verbose_name="Cour"
    def __str__(self):
        return f"{self.matiere} - {self.professeur} - {self.groupe}"
'''
class Groupe(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    matieres = models.ManyToManyField(Matiere, related_name='groupes')

    def __str__(self):
        return self.nom
'''

class Groupe(models.Model):
    nom = models.CharField(max_length=50)
    #niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)  # Choisir l'ID du niveau par défaut

    matieres = models.ManyToManyField(Matiere, related_name='groupes')
    class Meta:
        verbose_name="groupe"
    def __str__(self):
        return self.nom
    
class RunParam(models.Model):
    heure = models.OneToOneField(Heure, on_delete=models.CASCADE, blank=True ,null=True)
    niveau = models.OneToOneField(Niveau, on_delete=models.CASCADE, blank=True ,null=True)
    jours = models.OneToOneField(Jours, on_delete=models.CASCADE, blank=True ,null=True)
    class Meta:
        verbose_name="RunParam"
   