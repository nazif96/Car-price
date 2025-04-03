# Car-price 

## Contexte  

Ce projet a été réalisé dans le cadre d’un **projet académique** visant à mettre en pratique les compétences acquises en **data science**, notamment la collecte, le nettoyage, la modélisation et l’évaluation de données réelles.


## 📌 Objectif du projet

Ce projet a pour objectif de prédire le **prix des voitures d'occasion** à partir de caractéristiques disponibles telles que le kilométrage, la marque, l'année de mise en circulation, etc. Il repose sur un pipeline de data science structuré depuis la collecte des données jusqu’à la modélisation et l’évaluation des performances.

Réaliser une étude sur le marché des voitures d'occasions afin de déterminer quelles voitures ont des prix inférieurs selon les caractéristiques et de pouvoir réaliser de bonnes affaires sur le marché.

Notre comporte deux étapes:
1.  La collette des données via le `web Scraping` du site `https://www.autoscout24.be/fr/`
2.  Le `Machine Learning` des données pour la prédiction du prix de vente `prix`.


Le notebook principal **`Principal.ipynb`** centralise toutes les étapes clés du projet


## 🏗️ Structure du projet 

```
Car-price/
│
├── cleaning_data/                    # Scripts de nettoyage et de prétraitement des données
├── Donnees/                          # Fichiers de données brutes
├── machine_learning/                 # Scripts liés à l'entraînement la selection et évaluation des modèles
│   ├── machine.learn.py              # Fonctions d'entraînement / tuning
│   ├── train_model_utils.py          # Fonctions de chargement, best paramètre, réentrainement des modèles avec  etc.
|   ├── README.md                     # pour le machine learning
├── Modeles/                          # Modèles sauvegardés ou code spécifique aux modèles
├── Notebooks/                        # Jupyter Notebooks pour les explorations et machine learning 
├── Vehicles_scraping/                # Scripts de scraping des données de véhicules
├── venv/                             # Environnement virtuel Python
│
├── Principal.ipynb                   # Notebook principal de présentation du projet 
├── meilleur_modele_knn.pkl           # Meilleur modèle entraîné (KNN)
├── resultats_modeles.csv             # Comparatif des performances des modèles
├── LICENSE                           # Licence du projet
├── requirements.txt 
└── README.md                         # Description du projet
```


## 🔧 Étapes du pipeline (dans Principal.ipynb)

    1- Importation et exploration des données
    2- Nettoyage et traitement des données
    3- Feature engineering
    4- Séparation des données en train/test
    5- Entraînement de plusieurs modèles (KNN, Random Forest, etc.)
    6- Évaluation des performances
    7- Sauvegarde du meilleur modèle avec pickle
    8- Préparation à la mise en production


## 📊 Modèle final
Algorithme retenu : K-Nearest Neighbors (KNN)

Performance (score R² ou RMSE) : Voir le fichier resultats_modeles.csv

## ▶️ Lancer le projet

1. Cloner le dépôt :

```bash 
git clone https://github.com/ton-utilisateur/Car-price.git
cd Car-price
```
 
2. Créer un environnement virtuel :

```bash 
python -m venv venv
source venv/bin/activate  # sous Linux/Mac
venv\Scripts\activate
```

3. Installer les dépendances : 

```bash 
pip install -r requirements.txt
```

4. Ouvrir le notebook : 

```bash 
jupyter notebook Principal.ipynb

```

## 📌 Prochaines étapes

- Déploiement d'une API avec FastAPI

- Interface utilisateur avec Streamlit

- Intégration continue / CI

- Documentation plus complète


## 👨‍💻 Auteurs 

**AFOLABI Nazifou**

- **Datascientist | Machine Learning & Modeling** 
- Passionné par les sciences de données et l'intelligence artificielle.
- **Email** : [afolabinazif96@gmail.com](mailto.afolabinazif96@gmail.com)
- **LinkedIn** : [Nazifou AFOLABI](https://www.linkedin.com/in/nazifou-afolabi-10544729b/)
