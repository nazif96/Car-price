import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns 
import sympy as sp


#fonction de nettoyage pour analyse exploratoire des données

def stats_nettoie (df) :
    
    """Nettoyage""" 
    
    df.columns = df.columns.str.lower()
    df = df.drop(['date', 'version','vendeur', 'nom de la voiture'], axis=1) 
    df['prix'] = df['prix'].str.replace('€', '').str.replace(' ', '').str.replace(',', '.').astype(float)
    df['transmission'] = df['transmission'].replace(['- Boîte', 'Boite non disponible'], 'Autre')
    df['kilométrage'] = df['kilométrage'].str.replace('km', '').str.replace(' ', '').str.replace(',', '.').str.replace('- ', '0').astype(float)
    df['carburant'] = df['carburant'].replace(['- Carburant','CNG'], 'Autres')
    df['puissance'] = df['puissance'].str.extract('(\d+\.?\d*) CH').astype(float)
    df['évaluations'] = df['évaluations'].replace('Évaluations non disponibles', 0).astype(float)
    df= df.dropna(subset=['puissance'])
    
    return df

 






#fonction de nettoyage et de préparation des données

def nettoie_donnees (df) :
    
    """Nettoyage et préparation"""
    
    df.columns = df.columns.str.lower()
    df = df.drop(['date', 'version','vendeur', 'nom de la voiture'], axis=1) 
    df['prix'] = df['prix'].str.replace('€', '').str.replace(' ', '').str.replace(',', '.').astype(float)
    df['transmission'] = df['transmission'].replace(['- Boîte', 'Boite non disponible'], 'Autre')
    df['kilométrage'] = df['kilométrage'].str.replace('km', '').str.replace(' ', '').str.replace(',', '.').str.replace('- ', '0').astype(float)
    df['carburant'] = df['carburant'].replace(['- Carburant','CNG'], 'Autres')
    df['puissance'] = df['puissance'].str.extract('(\d+\.?\d*) CH').astype(float)
    df['évaluations'] = df['évaluations'].replace('Évaluations non disponibles', 0).astype(float)

    dt = pd.get_dummies(df, columns=['modèle', 'carburant', 'transmission'])
    df_encoded= dt.dropna(subset=['puissance'])
    df_encoded = df_encoded.drop('carburant_Autres', axis=1) 
    df_encoded = df_encoded.drop('transmission_Autre', axis=1)
    
    return df_encoded
