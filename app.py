import streamlit as st
from utils.file_processing import extract_text_from_files
from utils.gpt_interaction import generate_response

# Interface utilisateur avec Streamlit
st.title("ChatGPT Augmenté avec Téléchargement de Documents")
st.subheader("Discutez avec l'IA et téléchargez des documents pour un contexte supplémentaire")

# Sélecteur de modèle
model_options = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]
selected_model = st.selectbox("Sélectionnez le modèle", model_options)

# Sélecteur de nombre maximum de tokens
max_tokens_options = [50, 100, 150, 200, 250, 300, 350, 400, 450, 2500]
selected_max_tokens = st.selectbox("Nombre maximum de tokens", max_tokens_options, index=4)  # Par défaut à 250

# Champ pour le rôle
role_options = [
    "médecin",
    "avocat",
    "expert technique",
    "conseiller en finance",
    "professeur",
    "Autre"
]
selected_role = st.selectbox("Sélectionnez le rôle de l'IA", role_options)

if selected_role == "Autre":
    custom_role = st.text_input("Veuillez spécifier le rôle souhaité")
    if custom_role:
        selected_role = custom_role

# Zone de téléchargement de fichiers
uploaded_files = st.file_uploader("Glissez-déposez des fichiers ici ou cliquez pour télécharger", accept_multiple_files=True)

context = ""
if uploaded_files:
    context = extract_text_from_files(uploaded_files)

# Zone de chat
user_input = st.text_input("Vous :")
if user_input:
    response = generate_response(user_input, context, selected_model, selected_max_tokens, selected_role)
    st.text_area("ChatGPT :", value=response, height=200)
