import streamlit as st
import pandas as pd
import plotly.express as px

# Titre
st.title("📊 Dashboard d'analyse de données")

# Upload fichier
uploaded_file = st.file_uploader("Importer votre dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

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