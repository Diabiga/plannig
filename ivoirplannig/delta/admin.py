from django.contrib import admin
from delta.models import Matiere, Professeur, Grade , Salle, Batiment, Duree, Jours, Heure, Cours,Groupe





# Register your models here.
@admin.register(Matiere)
class planning2(admin.ModelAdmin):
    pass
@admin.register(Groupe)
class planningGroupe(admin.ModelAdmin):
    pass

@admin.register(Professeur)
class profModel(admin.ModelAdmin):
     list_display=("matricule","nom","prenom","grade")
     empty_value_display="inconnu"
  

@admin.register(Grade )
class gradeModel(admin.ModelAdmin):
    pass
@admin.register(Batiment)
class planning7(admin.ModelAdmin):
    pass



@admin.register(Duree)
class planning8(admin.ModelAdmin):
    pass



@admin.register(Jours)
class planning9(admin.ModelAdmin):
    pass


@admin.register(Heure)
class planning10(admin.ModelAdmin):
    pass


@admin.register(Cours)
class planning1(admin.ModelAdmin):
    pass

@admin.register(Salle)
class Salle(admin.ModelAdmin):
    list_display=("libelle","batiment")
    empty_value_display="inconnu"



'''




# Register your models here.

         
         
# Register your models here.



'''
