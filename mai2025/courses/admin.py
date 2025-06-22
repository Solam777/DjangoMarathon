from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Equipe, Membre, EntraineurMembre, Coureur, Ville, Etape, Court

# Equipe
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom')
    search_fields = ('code', 'nom')

# Membre (modèle de base)
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'appartient')
    list_filter = ('appartient',)
    search_fields = ('nom', 'prenom', 'email')
    raw_id_fields = ('appartient',)

# Entraineur
@admin.register(EntraineurMembre)
class EntraineurMembreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'appartient')
    list_filter = ('appartient',)
    search_fields = ('nom', 'prenom', 'email')

# Coureur
@admin.register(Coureur)
class CoureurAdmin(admin.ModelAdmin):
    list_display = ('dossard', 'nom', 'prenom', 'email', 'appartient', 'entraineur')
    list_filter = ('appartient', 'entraineur')
    search_fields = ('dossard', 'nom', 'prenom', 'email')
    raw_id_fields = ('appartient', 'entraineur')

# Ville
@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

# Etape
@admin.register(Etape)
class EtapeAdmin(admin.ModelAdmin):
    list_display = ('date', 'depart', 'arrive')
    list_filter = ('date',)
    date_hierarchy = 'date'
    raw_id_fields = ('depart', 'arrive')

# Court (participation aux étapes)
@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('coureur', 'etape', 'sortie')
    list_filter = ('etape', 'sortie')
    raw_id_fields = ('coureur', 'etape')