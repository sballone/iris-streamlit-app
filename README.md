# 🌸 Application d'Analyse du Dataset Iris

Application web interactive développée avec Streamlit pour l'analyse exploratoire du célèbre dataset Iris.

## 📋 Description

Cette application permet de visualiser et d'analyser le dataset Iris à travers différentes représentations graphiques :
- Distribution des espèces
- Histogrammes des variables
- Boîtes à moustaches (Boxplots)
- Nuages de points
- Matrices de corrélation
- Analyses avancées (Pairplot, Scatter matrix)

## 🚀 Installation et Exécution

### Prérequis
- Python 3.8 ou supérieur
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancement de l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

## 📁 Structure du projet

```
.
├── app.py              # Application Streamlit principale
├── requirements.txt    # Dépendances Python
├── iris.csv           # Dataset Iris (séparateur : point-virgule)
└── README.md          # Ce fichier
```

## 📊 Fonctionnalités

### 1. Aperçu des données
- Affichage des premières lignes
- Statistiques descriptives
- Informations sur le dataset

### 2. Distribution des espèces
- Graphique en barres
- Diagramme en secteurs
- Comptage des effectifs

### 3. Histogrammes
- Visualisation de la distribution de chaque variable
- Nombre de bins ajustable

### 4. Boxplots
- Comparaison des variables par espèce
- Détection des valeurs aberrantes
- Boxplots personnalisables

### 5. Nuages de points
- Relations entre variables
- Distinction par espèce
- Facettes par espèce

### 6. Corrélations
- Matrice de corrélation
- Heatmap des corrélations

### 7. Analyses avancées
- Pairplot complet
- Matrice de graphiques de dispersion

## 📦 Déploiement sur Streamlit Cloud

1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
2. Connectez votre dépôt GitHub
3. Sélectionnez le fichier `app.py`
4. Déployez !

**Important :** Assurez-vous que le fichier `iris.csv` est bien présent dans votre dépôt GitHub.

## 📝 Format du fichier CSV

Le fichier `iris.csv` doit utiliser le **point-virgule (;)** comme séparateur et contenir les colonnes suivantes :
- SepalLength
- SepalWidth
- PetalLength
- PetalWidth
- Species

Exemple :
```
SepalLength;SepalWidth;PetalLength;PetalWidth;Species
5.1;3.5;1.4;0.2;setosa
4.9;3.0;1.4;0.2;setosa
...
```

## 🛠️ Technologies utilisées

- **Streamlit** : Framework pour créer des applications web interactives
- **Pandas** : Manipulation et analyse de données
- **Seaborn** : Visualisations statistiques
- **Matplotlib** : Graphiques
- **NumPy** : Calculs numériques

## 👤 Auteur

sballone

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
