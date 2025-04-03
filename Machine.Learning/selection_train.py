import os
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
from scipy.optimize import minimize_scalar
import numpy as np
import pandas as pd
import joblib

from typing import Dict


def train_models_with_best_params(models: Dict[str, dict], X_train, y_train):
    trained_models = {}

    for model_name, params in models.items():
        # Copier les meilleurs paramètres
        raw_params = params["best_params"].copy()

        # Extraire la stratégie d'imputation
        imputation_strategy = raw_params.pop("imputation__strategy", "mean")

        # Nettoyer les clés : supprimer le préfixe 'entrainement__'
        model_params = {
            k.replace("entrainement__", ""): v
            for k, v in raw_params.items()
            if k.startswith("entrainement__")
        }

        # Créer une instance du modèle avec les bons paramètres
        model = params["model"](**model_params)

        # Construire le pipeline
        pipeline = Pipeline([
            ("imputation", SimpleImputer(strategy=imputation_strategy)),
            ("entrainement", model),
        ])

        # Entraîner le modèle
        pipeline.fit(X_train, y_train)

        # Stocker
        trained_models[model_name] = pipeline

    return trained_models


# Exemple d'utilisation :
#best_params = {
    #'Ridge': {'entrainement__alpha': 8, 'imputation__strategy': 'mean'},
    #'KNeighborsRegressor': {'entrainement__n_neighbors': 2, 'imputation__strategy': 'mean'},
    #'SVR': {'entrainement__C': 65536.0, 'entrainement__epsilon': 0.1, 'imputation__strategy': 'mean'},
    #'RandomForestRegressor': {'entrainement__max_features': None, 'entrainement__n_estimators': 100, 'imputation__strategy': 'median'},
    #'GradientBoostingRegressor': {'entrainement__learning_rate': 0.5, 'entrainement__n_estimators': 400, 'imputation__strategy': 'mean'},
    #'MLPRegressor': {'entrainement__hidden_layer_sizes': (50, 50), 'entrainement__max_iter': 1000, 'imputation__strategy': 'most_frequent'}
#}

#trained_models = train_models_with_best_params(best_params, X_train, y_train)