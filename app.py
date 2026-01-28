# Application Streamlit pour l'analyse du dataset Iris
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix

# Configuration de la page
st.set_page_config(
    page_title="Analyse du Dataset Iris",
    page_icon="🌸",
    layout="wide"
)

# Titre principal
st.title("🌸 Analyse Exploratoire du Dataset Iris")
st.markdown("---")

# Chargement des données
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('iris.csv', sep=';')
        return df
    except FileNotFoundError:
        st.error("⚠️ Fichier 'iris.csv' introuvable. Assurez-vous qu'il est dans le même dossier que app.py")
        return None

df = load_data()

if df is not None:
    # Sidebar pour la navigation
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Choisir une section:",
        ["📊 Aperçu des données", 
         "📈 Distribution des espèces", 
         "📉 Histogrammes",
         "📦 Boxplots",
         "🔵 Nuages de points",
         "🔗 Corrélations",
         "🎯 Analyses avancées"]
    )
    
    # Section 1: Aperçu des données
    if section == "📊 Aperçu des données":
        st.header("Aperçu des données")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Premières lignes du dataset")
            st.dataframe(df.head(10))
        
        with col2:
            st.subheader("Informations sur le dataset")
            st.write(f"**Nombre de lignes :** {df.shape[0]}")
            st.write(f"**Nombre de colonnes :** {df.shape[1]}")
            st.write(f"**Colonnes :** {', '.join(df.columns)}")
        
        st.subheader("Statistiques descriptives")
        st.dataframe(df.describe())
    
    # Section 2: Distribution des espèces
    elif section == "📈 Distribution des espèces":
        st.header("Distribution des espèces d'iris")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Effectifs par espèce (Barres)")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.countplot(x='Species', data=df, ax=ax, palette='viridis')
            ax.set_title('Effectifs par espèce')
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.subheader("Répartition en secteurs")
            fig, ax = plt.subplots(figsize=(8, 5))
            df['Species'].value_counts().plot.pie(
                autopct='%1.1f%%', 
                ax=ax, 
                colors=['#66b3ff','#99ff99','#ff9999']
            )
            ax.set_title('Répartition en secteurs')
            ax.set_ylabel('')
            st.pyplot(fig)
            plt.close()
        
        st.subheader("Nombre d'échantillons par espèce")
        st.dataframe(df['Species'].value_counts())
    
    # Section 3: Histogrammes
    elif section == "📉 Histogrammes":
        st.header("Histogrammes des variables quantitatives")
        
        variable = st.selectbox(
            "Sélectionner une variable:",
            ['PetalLength', 'PetalWidth', 'SepalLength', 'SepalWidth']
        )
        
        bins = st.slider("Nombre de bins:", min_value=5, max_value=30, value=10)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(df[variable], bins=bins, color='steelblue', edgecolor='black')
        ax.set_title(f"Histogramme de {variable}")
        ax.set_xlabel(variable)
        ax.set_ylabel("Effectif")
        st.pyplot(fig)
        plt.close()
    
    # Section 4: Boxplots
    elif section == "📦 Boxplots":
        st.header("Boîtes à moustaches (Boxplots)")
        st.markdown("Les boxplots permettent de visualiser la distribution d'une variable quantitative en fonction d'une variable qualitative.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Longueur des pétales par espèce")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='Species', y='PetalLength', ax=ax, palette='Set2')
            ax.set_title('Boxplot de la longueur des pétales par espèce')
            st.pyplot(fig)
            plt.close()
            st.info("💡 On observe des différences significatives entre les espèces.")
        
        with col2:
            st.subheader("Largeur des sépales par espèce")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='Species', y='SepalWidth', ax=ax, palette='Set2')
            ax.set_title('Boxplot de la largeur des sépales par espèce')
            st.pyplot(fig)
            plt.close()
            st.info("💡 La largeur des sépales varie selon l'espèce, avec des médianes et des étendues différentes.")
        
        # Option pour choisir d'autres variables
        st.subheader("Boxplot personnalisé")
        variable_y = st.selectbox(
            "Choisir une variable à analyser:",
            ['PetalLength', 'PetalWidth', 'SepalLength', 'SepalWidth']
        )
        
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='Species', y=variable_y, ax=ax, palette='coolwarm')
        ax.set_title(f'Boxplot de {variable_y} par espèce')
        st.pyplot(fig)
        plt.close()
    
    # Section 5: Nuages de points
    elif section == "🔵 Nuages de points":
        st.header("Nuages de points")
        
        # Nuage de points avec distinction par espèce
        st.subheader("Sépales : Longueur vs Largeur")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x='SepalLength', y='SepalWidth', hue='Species', style='Species', s=100, ax=ax)
        ax.set_title('Nuage de points de la longueur et largeur des sépales par espèce')
        st.pyplot(fig)
        plt.close()
        
        # Nuage de points pour les pétales
        st.subheader("Pétales : Longueur vs Largeur")
        fig, ax = plt.subplots(figsize=(10, 6))
        for esp in df["Species"].unique():
            sous_df = df[df["Species"] == esp]
            ax.scatter(
                sous_df["PetalLength"],
                sous_df["PetalWidth"],
                label=esp,
                s=100,
                alpha=0.7
            )
        ax.set_title("Nuage de points pétales avec distinction par espèce")
        ax.set_xlabel("Longueur du pétale (cm)")
        ax.set_ylabel("Largeur du pétale (cm)")
        ax.legend()
        st.pyplot(fig)
        plt.close()
        
        # FacetGrid
        st.subheader("Facettes par espèce")
        g = sns.FacetGrid(df, col='Species', height=4)
        g.map(sns.scatterplot, 'SepalLength', 'SepalWidth')
        g.add_legend()
        st.pyplot(g.fig)
        plt.close()
    
    # Section 6: Corrélations
    elif section == "🔗 Corrélations":
        st.header("Corrélations entre variables quantitatives")
        
        correlation = df.drop("Species", axis=1).corr()
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Matrice de corrélation")
            st.dataframe(correlation.style.background_gradient(cmap='coolwarm', axis=None))
        
        with col2:
            st.subheader("Heatmap des corrélations")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, ax=ax, fmt='.2f')
            ax.set_title('Heatmap des corrélations')
            st.pyplot(fig)
            plt.close()
        
        st.info("💡 Les variables liées aux pétales (PetalLength et PetalWidth) sont fortement corrélées.")
    
    # Section 7: Analyses avancées
    elif section == "🎯 Analyses avancées":
        st.header("Analyses avancées")
        
        # Pairplot
        st.subheader("Pairplot - Relations entre toutes les variables")
        st.info("⏳ Génération du graphique en cours... Cela peut prendre quelques secondes.")
        
        fig = sns.pairplot(df, hue='Species', height=2.5)
        fig.fig.suptitle('Pairplot des variables en fonction de l\'espèce', y=1.02)
        st.pyplot(fig.fig)
        plt.close()
        
        st.markdown("---")
        
        # Scatter matrix
        st.subheader("Matrice de graphiques de dispersion")
        fig, axes = plt.subplots(4, 4, figsize=(12, 12))
        scatter_matrix(df.drop("Species", axis=1), ax=axes, diagonal='kde', alpha=0.7)
        plt.suptitle('Matrice de graphiques de dispersion', y=0.995)
        st.pyplot(fig)
        plt.close()
        
        st.success("✅ Ces représentations permettent de visualiser les relations entre toutes les variables quantitatives et de voir comment elles varient en fonction de l'espèce. Par exemple, Setosa est bien séparée des autres dans plusieurs dimensions, alors que Versicolor et Virginica se chevauchent davantage.")

else:
    st.warning("Impossible de charger les données. Vérifiez que le fichier 'iris.csv' est présent.")

# Footer
st.markdown("---")
st.markdown("💻 Application développée avec Streamlit | 🌸 Dataset Iris")
