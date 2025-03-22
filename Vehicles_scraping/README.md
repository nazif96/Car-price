## Vehicles Scraping 

L'extraction des données via site web `AutoScout24.com` pour construire un dataset structuré  avec comme variables les différents caractéristiques (prix, kilométrage, année, etc) des automobiles du site.

### 🏗️structure du dossier 
```
Vehicle_scraping/
│
├── data/
│   ├── vehicules.csv            # Fichier généré automatiquement
│   ├── vehicules.json           # Idem
|
├── scraper/
│   ├── __init__.py
│   ├── scraper_methods.py       # Fonctions utilitaires (HTML, JSON)
│   ├── VehicleScraper.py        # Classe principale
│
│
├── main.py                      # Script principal à exécuter
└── README.md                    # (optionnel) instructions d’utilisation
```

### Mise en place du scraping 

- `scraper_methods.py` : contient deux fonctions utilitaires simples mais essentielles.
    - `get_html()` : récupérer proprement le HTML d’une page pour le parsing.
    - `save_to_json()` : stocker n’importe quelle structure de données en JSON lisible.

- `VehicleScraper.py`  contient 
    - le Classe `VehicleScraper` qui initialise l'objet avec une liste d'urls
    - scrape_vehicles(self, url, page) qui Scrape les données d’une seule page de résultats d’un modèle de voiture.
    - Utilise BeautifulSoup pour parser le HTML, puis boucle sur chaque <article> (chaque véhicule).

        Pour chaque article, il extrait :
        Prix (_extract_price)

        Transmission (_extract_transmission)

        Kilométrage (_extract_mileage)

        Carburant (_extract_fuel)

        Puissance (_extract_power)

        Nombre d’évaluations (_extract_evaluation_count)

        Version (_extract_version_element)

        Nom du vendeur (_extract_seller_name_element)

        Nom complet du véhicule (_extract_car_name_version)

        Date de mise en circulation (_extract_date)

Tous ces éléments sont ajoutés dans une liste de tuples vehicles.

- `Fonctions privées d'extraction (_extract_*)`
    Chacune cherche une info spécifique à l’intérieur de l’article HTML 

En somme: 
    - Scrape des pages d’annonces de voitures.
    - Extrait proprement les données en structurant tout dans des tuples.
    - Peut traiter plusieurs modèles de voitures et plusieurs pages pour chaque modèle.
    - Organise tout dans un dict avec les modèles en clés.

- `main.py` :
    - Définir une liste d’URLs de modèles de voitures.
    - puis lance la scraping la classe `VehicleScraper` defint dans `VehicleScraper.py `
    - Sauvegarder les données dans un fichier CSV et un fichier JSON.


| Fichier              | Rôle                                              | À exécuter ?                    |
|----------------------|---------------------------------------------------|---------------------------------|
| `scraper_methods.py` | Fonctions utilitaires (requête HTML, JSON)        | ❌ (juste utilisé, pas exécuté) |
| `VehicleScraper.py`  | Classe principale pour faire le scraping          | ❌ (importé uniquement)         |
| `main_.py`    | Script qui lance tout le processus de scraping    | ✅ À exécuter uniquement         |


pour lancer le scraping il nous faut juste lancer dans le terminale le code suivant 

```bash
python main.py  
```