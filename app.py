import streamlit as st
from utils.file_processing import extract_text_from_files
from utils.gpt_interaction import generate_response

# Interface utilisateur avec Streamlit
st.title("ChatGPT Augmenté avec Téléchargement de Documents")
st.subheader("Discutez avec l'IA et téléchargez des documents pour un contexte supplémentaire")

# Zone de téléchargement de fichiers
uploaded_files = st.file_uploader("Glissez-déposez des fichiers ici ou cliquez pour télécharger", accept_multiple_files=True)

context = ""
if uploaded_files:
    context = extract_text_from_files(uploaded_files)

# Zone de chat
user_input = st.text_input("Vous :")
if user_input:
    response = generate_response(user_input, context)
    st.text_area("ChatGPT :", value=response, height=200)
