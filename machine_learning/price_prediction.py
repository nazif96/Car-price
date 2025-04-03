def predict_price(modele, voiture_dict, colonnes_reference):
    """
    Prédit le prix d'une voiture à partir d'un dictionnaire de caractéristiques.
    
    - modele : pipeline entraîné (ex : modele_knn)
    - voiture_dict : dictionnaire contenant les features de la voiture
    - colonnes_reference : colonnes utilisées à l'entraînement (X_test.columns)
    """
    import pandas as pd
    import numpy as np

    df_voiture = pd.DataFrame([voiture_dict])

    # Compléter les colonnes manquantes (ex : one-hot encoding)
    cols_manquantes = [col for col in colonnes_reference if col not in df_voiture.columns]
    df_manquantes = pd.DataFrame(0, index=np.arange(len(df_voiture)), columns=cols_manquantes)

    # Fusionner et réaligner les colonnes
    df_complet = pd.concat([df_voiture, df_manquantes], axis=1)
    df_complet = df_complet.reindex(columns=colonnes_reference, fill_value=0)

    # Prédiction
    prix = modele.predict(df_complet)
    return prix[0]



#voiture_exemple = {
    #'Modèle': 'bentley',
    #'Kilométrage': 10000,
    #'Puissance_CH': 500,
    #'Transmission_Boîte automatique': True
#}

#prix_predit = predict_price(modele_knn, voiture_exemple, X_test.columns)
#print("💰 Prix prédit :", round(prix_predit, 2))
