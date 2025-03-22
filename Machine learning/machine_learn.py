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

MODELS_DIR = "Modeles"

def train_and_optimize_model(model, param_grid, X_train, y_train, model_name):
    pipeline = Pipeline([
        ("imputation", SimpleImputer()),
        ("entrainement", model),
    ])

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
    )

    grid_search.fit(X_train, y_train)

    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)

    model_path = os.path.join(MODELS_DIR, f"{model_name}_model.pkl")
    joblib.dump(grid_search, model_path)

    return grid_search

def optimize_svr_params(X_train, y_train):
    for strategy in ["mean", "median", "most_frequent"]:
        for echelle in [MinMaxScaler, StandardScaler]:
            def objective(c):
                svr = Pipeline([
                    ("imputation", SimpleImputer(strategy=strategy)),
                    ("echelle", echelle()),
                    ("entrainement", SVR(C=c)),
                ])
                return -cross_val_score(svr, X_train, y_train).mean()

            result = minimize_scalar(fun=objective, bounds=(1, 1000000), method="bounded")
            print(strategy, str(echelle), result.x, -result.fun)

def train_best_models(X_train, y_train):
    ridge_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__alpha": [2 ** p for p in range(-6, 7)],
    }
    ridge_model = train_and_optimize_model(Ridge(), ridge_params, X_train, y_train, "ridge")

    knr_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__n_neighbors": range(2, 15),
    }
    knr_model = train_and_optimize_model(KNeighborsRegressor(), knr_params, X_train, y_train, "kneighbors")

    svr_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__C": np.logspace(-4, 16, 15, base=2),
        "entrainement__epsilon": [0.1, 0.4, 0.7],
    }
    svr_model = train_and_optimize_model(SVR(), svr_params, X_train, y_train, "svr")

    rfr_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__n_estimators": range(50, 200, 10),
        "entrainement__max_features": [None],
    }
    rfr_model = train_and_optimize_model(RandomForestRegressor(), rfr_params, X_train, y_train, "random_forest")

    gbr_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__learning_rate": (0.005, 0.01, 0.1, 0.5),
        "entrainement__n_estimators": (50, 100, 150, 200, 400),
    }
    gbr_model = train_and_optimize_model(GradientBoostingRegressor(), gbr_params, X_train, y_train, "gradient_boosting")

    mlp_params = {
        "imputation__strategy": ["mean", "median", "most_frequent"],
        "entrainement__hidden_layer_sizes": [(100,), (150,), (300,), (500,), (50, 50)],
        "entrainement__max_iter": [1000],
    }
    mlp_model = train_and_optimize_model(MLPRegressor(), mlp_params, X_train, y_train, "mlp")

    return ridge_model, knr_model, svr_model, rfr_model, gbr_model, mlp_model

# Appel de la fonction train_best_models
#ridge_model, knr_model, svr_model, rfr_model, gbr_model, mlp_model = train_best_models(X_train, y_train)

