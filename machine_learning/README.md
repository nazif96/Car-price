## Prédiction du Prix d’un Bien  (Machine Learning)

### 🎯 Objectif
Ce projet a pour objectif de développer et comparer plusieurs modèles de régression supervisée afin de prédire le prix d’un bien (voiture, logement, produit, etc.) à partir de ses caractéristiques.

### 🔍 Contexte
La prédiction précise des prix permet de :

Aider les entreprises à ajuster leurs offres commerciales

Optimiser les politiques de tarification dynamique

Fournir aux utilisateurs finaux une estimation fiable basée sur des données réelles

`mais dans notre cas est de voir si l'achat serait une bonne ou mauvaise affaire` 

###  Technologies utilisées
- Python 3
- Scikit-learn : pipelines, modèles de ML, grid search
- Pandas / NumPy : manipulation de données
- Matplotlib / Seaborn : visualisation
- Joblib : sauvegarde des modèles
- Jupyter Notebook / Streamlit (optionnel) : interface d’analyse

### 🧪 Méthodologie
1. Prétraitement des données

Nettoyage, imputation des valeurs manquantes

Séparation des variables explicatives (X) et de la cible (y)

2. Division des données

train_test_split (80% entraînement / 20% test)

3. Sélection de modèles

Ridge Regression(Ridge), K-Nearest Neighbors Regressor(KNN), Support Vector Regressor(SVR), Random Forest(rf), Gradient Boosting Regressor(), Multi-Layer Perceptron (Mlp)

3. Optimisation des hyperparamètres

Utilisation de GridSearchCV avec validation croisée

Recherche des meilleurs paramètres pour chaque modèle

4. Réentraînement final

Chaque modèle est réentraîné avec ses meilleurs paramètres

5. Évaluation finale

Calcul des métriques sur le test set :

RMSE (Root Mean Squared Error)

MAE (Mean Absolute Error)

R² (Score de détermination)

6. Comparaison des performances

Visualisation des RMSE par modèle

Export des résultats au format .csv



NB: les fichier Ml doit etre deplacer sur  la racine du projet pour utilisation. 

