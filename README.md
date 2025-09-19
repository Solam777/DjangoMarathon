# DjangoMarathon

DjangoMarathon est une application web développée avec **Django** pour gérer des courses de marathon, leurs coureurs, équipes, étapes, et résultats.  

---

## 📋 Fonctionnalités principales

- Gestion des équipes (`Equipe`)  
- Gestion des membres (`Membre`), y compris les entraineurs et les coureurs  
- Attribution des dossards, affiliation des coureurs à une équipe et un entraineur  
- Gestion des villes et des étapes de course entre villes (départ / arrivée)  
- Enregistrement des résultats **ou** des sorties (abandon, accident, disqualification) pour chaque coureur dans chaque étape  

---

## 🗂 Architecture (modèles / base de données)

Voici les modèles principaux :

| Modèle            | Champs notables / relations                              |
|------------------|------------------------------------------------------------|
| Equipe           | `code` (unique), `nom`                                     |
| Membre           | `nom`, `prenom`, `email`, appartient à une `Equipe`        |
| EntraineurMembre | extension de `Membre`                                      |
| Coureur          | `dossard`, lié à un `EntraineurMembre`                     |
| Ville            | `nom`                                                      |
| Etape            | date, `depart` (Ville), `arrivee` (Ville)                  |
| Court            | `coureur`, `etape`, champ `sortie` (Enum)                  |

---

## ⚙️ Installation et configuration

Voici comment démarrer le projet en local :

1# Cloner le dépôt
git clone https://github.com/Solam777/DjangoMarathon.git
cd DjangoMarathon/mai2025

# Créer un environnement virtuel (optionnel mais recommandé)
python3 -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur pour accéder à l’admin
python manage.py createsuperuser

# Démarrer le serveur de développement
python manage.py runserver

# Go to 
http://127.0.0.1:8000/admin/
