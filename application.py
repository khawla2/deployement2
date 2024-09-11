import streamlit as st
import pandas as pd
import joblib

# Configuration de la page
st.set_page_config(
    page_title="Classification de la Qualité des Produits Cimentiers",
    page_icon=":factory:",
    layout='wide',
    initial_sidebar_state='expanded'
)

# Charger les modèles
rc2_model = joblib.load('RC2_classification_randomforest.pkl')['random_forest']
rc28_model = joblib.load('RC28_classification_randomforest.pkl')['random_forest']

# Charger les données
data = pd.read_excel('Base de donnée Stage.xlsx', header=2)

# Chargement du CSS personnalisé
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Affichage du logo dans la barre latérale
st.sidebar.image('cimar.png')

# Options de la barre latérale avec boutons radio
st.sidebar.subheader('Sélectionnez une page')
page = st.sidebar.radio(
    'Choisissez une option', 
    ['Accueil', 'Classification avec RC2j', 'Classification avec RC28j'],
    format_func=lambda x: x[:30] + '...' if len(x) > 30 else x
)

# Fonction pour afficher la page d'accueil
def home():
    st.markdown("""
        <div class="main-content">
            <div class="app-background">
                <div class="rectangle">
                    <h1 class="title">Classification des produits cimentiers CPJ45 de l'usine de Jorf</h1>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Fonction pour afficher la page RC2j
def rc2_page():
    st.title("Classification des produits cimentiers en se basant sur RC2j")
    st.write("Veuillez entrer s'il vous plaît les valeurs demandées :")

    # Création des champs de saisie
    with st.form(key='rc2_form'):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            PAF_CV = st.number_input('PAF CV', value=0.0)
            SiO2 = st.number_input('SiO2', value=0.0)
            Al2O3 = st.number_input('Al2O3', value=0.0)
            Fe2O3 = st.number_input('Fe2O3', value=0.0)
            CaO = st.number_input('CaO', value=0.0)
            MgO = st.number_input('MgO', value=0.0)
            SO3_cl = st.number_input('SO3 cl', value=0.0)
            K2O = st.number_input('K2O', value=0.0)
            PAF_cl = st.number_input('PAF cl', value=0.0)
            CaOl = st.number_input('CaOl', value=0.0)
            C3A = st.number_input('C3A', value=0.0)
            C3S = st.number_input('C3S', value=0.0)
            SO3_g = st.number_input('SO3 g', value=0.0)

        with col2:
            percent_clinker = st.number_input('%clinker', value=0.0)
            percent_CV = st.number_input('% CV', value=0.0)
            percent_gypse = st.number_input('% gypse', value=0.0)
            Refus_40_m = st.number_input('Refus 40 μm', value=0.0)

        # Bouton de soumission centré et en jaune
        submit_button = st.form_submit_button("Soumettre")

        if submit_button:
            input_data = pd.DataFrame({
                'PAF CV ': [PAF_CV],
                'SiO2': [SiO2],
                'Al2O3': [Al2O3],
                'Fe2O3': [Fe2O3],
                'CaO': [CaO],
                'MgO': [MgO],
                'SO3 cl': [SO3_cl],
                'K2O': [K2O],
                'PAF cl': [PAF_cl],
                'CaOl ': [CaOl],
                'C3A': [C3A],
                'C3S': [C3S],
                'SO3 g': [SO3_g],
                '%clinker': [percent_clinker],
                '% CV': [percent_CV],
                '% gypse': [percent_gypse],
                'Refus 40 μm': [Refus_40_m]
            })

            prediction = rc2_model.predict(input_data)

            # Affichage du résultat avec icônes
            if prediction[0] == 1:
                st.success("✅ Vu que la résistance RC2j dépasse 13.5 MPa, alors votre produit est de bonne qualité.")
            else:
                st.error("❌ Vu que la résistance RC2j est inférieure à 13.5 MPa, alors votre produit n'est pas de bonne qualité.")

# Fonction pour afficher la page RC28j
def rc28_page():
    st.title("Classification des produits cimentiers en se basant sur RC28j")
    st.write("Veuillez entrer s'il vous plaît les valeurs demandées :")

    with st.form(key='rc28_form'):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            PAF_CV = st.number_input('PAF CV', value=0.0)
            SiO2 = st.number_input('SiO2', value=0.0)
            Al2O3 = st.number_input('Al2O3', value=0.0)
            Fe2O3 = st.number_input('Fe2O3', value=0.0)
            CaO = st.number_input('CaO', value=0.0)
            MgO = st.number_input('MgO', value=0.0)
            SO3_cl = st.number_input('SO3 cl', value=0.0)
            K2O = st.number_input('K2O', value=0.0)
            PAF_cl = st.number_input('PAF cl', value=0.0)
            CaOl = st.number_input('CaOl', value=0.0)
            C3A = st.number_input('C3A', value=0.0)
            C3S = st.number_input('C3S', value=0.0)
            SO3_g = st.number_input('SO3 g', value=0.0)

        with col2:
            percent_clinker = st.number_input('%clinker', value=0.0)
            percent_CV = st.number_input('% CV', value=0.0)
            percent_gypse = st.number_input('% gypse', value=0.0)
            Refus_40_m = st.number_input('Refus 40 μm', value=0.0)

        # Bouton de soumission centré et en jaune
        submit_button = st.form_submit_button("Soumettre")

        if submit_button:
            input_data = pd.DataFrame({
                'PAF CV ': [PAF_CV],
                'SiO2': [SiO2],
                'Al2O3': [Al2O3],
                'Fe2O3': [Fe2O3],
                'CaO': [CaO],
                'MgO': [MgO],
                'SO3 cl': [SO3_cl],
                'K2O': [K2O],
                'PAF cl': [PAF_cl],
                'CaOl ': [CaOl],
                'C3A': [C3A],
                'C3S': [C3S],
                'SO3 g': [SO3_g],
                '%clinker': [percent_clinker],
                '% CV': [percent_CV],
                '% gypse': [percent_gypse],
                'Refus 40 μm': [Refus_40_m]
            })

            prediction = rc28_model.predict(input_data)

            # Affichage du résultat avec icônes
            if prediction[0] == 1:
                st.success("✅ Vu que la résistance RC28j varie entre 34 et 55 MPa, alors votre produit est de bonne qualité.")
            else:
                st.error("❌ Votre produit n'est pas de bonne qualité.")

# Appel de la fonction en fonction de la sélection
if page == 'Accueil':
    home()
elif page == 'Classification avec RC2j':
    rc2_page()
elif page == 'Classification avec RC28j':
    rc28_page()
