import pandas as pd
import numpy as np

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





def analyser_prix_prediction(modele, voiture_exemple: dict, colonnes_reference, df: pd.DataFrame):
    """
    Prédit le prix d'une voiture et le compare aux voitures similaires du dataset df.
    
    Paramètres :
        modele : modèle pipeline entraîné (ex: KNN)
        voiture_exemple : dictionnaire avec les caractéristiques de la voiture
        colonnes_reference : colonnes du jeu d'entraînement (ex: X_train.columns)
        df : ton DataFrame contenant les données encodées + la colonne 'prix'
    """
    # 1. Créer le DataFrame pour la voiture
    df_voiture = pd.DataFrame([voiture_exemple])

    # 2. Compléter les colonnes manquantes
    cols_manquantes = [col for col in colonnes_reference if col not in df_voiture.columns]
    df_manquantes = pd.DataFrame(0, index=[0], columns=cols_manquantes)

    df_voiture_encoded = pd.concat([df_voiture, df_manquantes], axis=1)
    df_voiture_encoded = df_voiture_encoded.reindex(columns=colonnes_reference, fill_value=0)

    # 3. Prédire le prix
    prix_predit = modele.predict(df_voiture_encoded)[0]
    print(f"💰 Prix prédit : {round(prix_predit, 2)} €")

    # 4. Extraire les critères
    modele_col = voiture_exemple.get("modèle", None)
    kilometrage = voiture_exemple.get("kilométrage", None)
    puissance = voiture_exemple.get("puissance", None)

    if modele_col and kilometrage and puissance:
        km_min = kilometrage * 0.85
        km_max = kilometrage * 1.15
        puiss_min = puissance * 0.9
        puiss_max = puissance * 1.1

        # 5. Filtrer les voitures similaires dans df
        voitures_similaires = df[
            (df[modele_col] == 1) &
            (df['kilométrage'].between(km_min, km_max)) &
            (df['puissance'].between(puiss_min, puiss_max))
        ]

        if not voitures_similaires.empty:
            prix_moyen = voitures_similaires['prix'].mean()
            prix_min = voitures_similaires['prix'].min()
            prix_max = voitures_similaires['prix'].max()

            print(f"\n📊 Voitures similaires trouvées : {len(voitures_similaires)}")
            print(f"📌 Prix moyen observé : {round(prix_moyen, 2)} €")
            print(f"🔻 Prix minimum : {round(prix_min, 2)} €")
            print(f"🔺 Prix maximum : {round(prix_max, 2)} €")

            if prix_predit < prix_moyen:
                print("✅ Le prix prédit est **inférieur** au marché → bonne affaire.")
            elif prix_predit > prix_moyen:
                print("⚠️ Le prix prédit est **supérieur** au marché → à surveiller.")
            else:
                print("🔸 Le prix prédit correspond exactement au prix moyen.")
        else:
            print("❌ Aucune voiture similaire trouvée dans le dataset.")
    else:
        print("⚠️ Informations manquantes (modèle, puissance, kilométrage).")



#voiture_exemple = {
    #'Modèle': 'bentley',
    #'Kilométrage': 10000,
    #'Puissance_CH': 500,
    #'Transmission_Boîte automatique': True
#}

#prix_predit = predict_price(modele_knn, voiture_exemple, X_test.columns)
#print("💰 Prix prédit :", round(prix_predit, 2))
