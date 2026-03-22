import streamlit as st
import pandas as pd
import plotly.express as px

# Titre
st.title("📊 Dashboard d'analyse de données")import streamlit as st
import pandas as pdimport streamlit as st
import pandas as pd
import plotly.express as px

# Titre
st.title("📊 Dashboard d'analyse de données")

# 🔥 CHANGEMENT ICI : chargement direct du fichier
df = pd.read_csv("Dataset.csv")

st.subheader("Aperçu des données")
st.dataframe(df)

# Colonnes
num_cols = df.select_dtypes(include='number').columns
cat_cols = df.select_dtypes(include='object').columns

# Sidebar filtres
st.sidebar.header("Filtres")

if len(cat_cols) > 0:
    selected_cat = st.sidebar.selectbox("Choisir une catégorie", cat_cols)
    unique_vals = df[selected_cat].dropna().unique()
    selected_val = st.sidebar.selectbox("Valeur", unique_vals)

    df = df[df[selected_cat] == selected_val]

st.subheader("Données filtrées")
st.dataframe(df)

# Graphique interactif
if len(num_cols) >= 2:
    st.subheader("Graphique interactif")

    x_axis = st.selectbox("Axe X", num_cols)
    y_axis = st.selectbox("Axe Y", num_cols)

    fig = px.scatter(df, x=x_axis, y=y_axis, color=x_axis)
    st.plotly_chart(fig)

# Histogramme
if len(cat_cols) > 0:
    st.subheader("Distribution")
    fig2 = px.histogram(df, x=cat_cols[0])
    st.plotly_chart(fig2)
import plotly.express as px

# Configuration page
st.set_page_config(page_title="Dashboard Data", layout="wide")

# Titre
st.title("📊 Dashboard d'analyse de données")

# Chargement des données (local)
data = pd.read_csv("Dataset.csv")

# Aperçu
st.subheader("📁 Aperçu du dataset")
st.dataframe(df)

# Colonnes
num_cols = df.select_dtypes(include='number').columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()

# Sidebar filtres
st.sidebar.header("🔍 Filtres")

df_filtered = df.copy()

if len(cat_cols) > 0:
    selected_cat = st.sidebar.selectbox("Choisir une variable catégorielle", cat_cols)
    values = df[selected_cat].dropna().unique()

    selected_values = st.sidebar.multiselect("Choisir valeur(s)", values, default=values)

    df_filtered = df_filtered[df_filtered[selected_cat].isin(selected_values)]

# Affichage filtré
st.subheader("📊 Données filtrées")
st.dataframe(df_filtered)

# Graphique interactif
if len(num_cols) >= 2:
    st.subheader("📈 Analyse interactive")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox("Axe X", num_cols)

    with col2:
        y_axis = st.selectbox("Axe Y", num_cols)

    fig = px.scatter(
        df_filtered,
        x=x_axis,
        y=y_axis,
        color=x_axis,
        title="Relation entre variables"
    )

    st.plotly_chart(fig, use_container_width=True)

# Histogramme
if len(cat_cols) > 0:
    st.subheader("📊 Distribution des catégories")

    fig2 = px.histogram(
        df_filtered,
        x=cat_cols[0],
        title="Répartition des données"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Corrélation
if len(num_cols) > 1:
    st.subheader("🔥 Matrice de corrélation")

    corr = df_filtered[num_cols].corr()

    fig3 = px.imshow(
        corr,
        text_auto=True,
        title="Corrélation entre variables"
    )

    st.plotly_chart(fig3, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Projet Data Science - Analyse & Visualisation")

# Upload fichier
uploaded_file = st.file_uploader("Importer votre dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv("Dataset.csv")

    st.subheader("Aperçu des données")
    st.dataframe(df)

    # Colonnes
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    # Sidebar filtres
    st.sidebar.header("Filtres")

    if len(cat_cols) > 0:
        selected_cat = st.sidebar.selectbox("Choisir une catégorie", cat_cols)
        unique_vals = df[selected_cat].dropna().unique()
        selected_val = st.sidebar.selectbox("Valeur", unique_vals)

        df = df[df[selected_cat] == selected_val]

    st.subheader("Données filtrées")
    st.dataframe(df)

    # Graphique interactif
    if len(num_cols) >= 2:
        st.subheader("Graphique interactif")

        x_axis = st.selectbox("Axe X", num_cols)
        y_axis = st.selectbox("Axe Y", num_cols)

        fig = px.scatter(df, x=x_axis, y=y_axis, color=x_axis)
        st.plotly_chart(fig)

    # Histogramme
    if len(cat_cols) > 0:
        st.subheader("Distribution")
        fig2 = px.histogram(df, x=cat_cols[0])
        st.plotly_chart(fig2)

else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
