
import os
import joblib
import pandas as pd
from typing import Dict
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




# model_utils.py



def load_all_models(models_dir="Modeles") -> dict:
    """
    Charge tous les fichiers .pkl dans un dossier donné
    Retourne un dictionnaire {nom_du_modele: objet GridSearchCV}
    """
    loaded_models = {}

    if not os.path.exists(models_dir):
        print(f"📁 Dossier '{models_dir}' introuvable.")
        return loaded_models

    for file in os.listdir(models_dir):
        if file.endswith("_model.pkl"):
            model_name = file.replace("_model.pkl", "")
            model_path = os.path.join(models_dir, file)
            loaded_models[model_name] = joblib.load(model_path)

    return loaded_models

def get_all_best_params(loaded_models: dict) -> dict:
    """
    Extrait les meilleurs hyperparamètres depuis les objets GridSearchCV chargés.
    Retourne un dictionnaire {nom_du_modele: best_params_ dict}
    """
    best_params_dict = {}

    for name, model in loaded_models.items():
        if hasattr(model, "best_params_"):
            best_params_dict[name] = model.best_params_
        else:
            print(f"⚠️ Le modèle '{name}' n'a pas d'attribut best_params_.")

    return best_params_dict

def extract_best_params_dict(gridsearch_models: dict) -> dict:
    """
    Construit un dictionnaire {nom_modele: {model: class, best_params: dict}}
    à partir de GridSearchCV
    """
    models_dict = {}

    for name, gridsearch in gridsearch_models.items():
        model_class = gridsearch.estimator.named_steps["entrainement"].__class__
        best_params = gridsearch.best_params_

        models_dict[name] = {
            "model": model_class,
            "best_params": best_params
        }

    return models_dict

def train_models_with_best_params(models: Dict[str, dict], X_train, y_train) -> dict:
    """
    Réentraîne les modèles avec leurs meilleurs hyperparamètres sur X_train.
    Retourne un dictionnaire {nom_modele: pipeline entraîné}
    """
    trained_models = {}

    for model_name, params in models.items():
        raw_params = params["best_params"].copy()
        imputation_strategy = raw_params.pop("imputation__strategy", "mean")

        model_params = {
            k.replace("entrainement__", ""): v
            for k, v in raw_params.items()
            if k.startswith("entrainement__")
        }

        model = params["model"](**model_params)

        pipeline = Pipeline([
            ("imputation", SimpleImputer(strategy=imputation_strategy)),
            ("entrainement", model),
        ])

        pipeline.fit(X_train, y_train)
        trained_models[model_name] = pipeline

    return trained_models

def best_params_to_dataframe(best_params: dict) -> pd.DataFrame:
    """
    Transforme un dict de best_params en DataFrame transposé pour affichage
    """
    return pd.DataFrame(best_params).T


 Exemple d'utilisation :
#best_params = {
    #'Ridge': {'entrainement__alpha': 8, 'imputation__strategy': 'mean'},
    #'KNeighborsRegressor': {'entrainement__n_neighbors': 2, 'imputation__strategy': 'mean'},
    #'SVR': {'entrainement__C': 65536.0, 'entrainement__epsilon': 0.1, 'imputation__strategy': 'mean'},
    #'RandomForestRegressor': {'entrainement__max_features': None, 'entrainement__n_estimators': 100, 'imputation__strategy': 'median'},
    #'GradientBoostingRegressor': {'entrainement__learning_rate': 0.5, 'entrainement__n_estimators': 400, 'imputation__strategy': 'mean'},
    #'MLPRegressor': {'entrainement__hidden_layer_sizes': (50, 50), 'entrainement__max_iter': 1000, 'imputation__strategy': 'most_frequent'}
#}

#from machine_learning.selection_train import train_models_with_best_params
#trained_models = train_models_with_best_params(models_dict, X_train, y_train)