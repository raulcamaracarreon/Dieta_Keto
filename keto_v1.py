# Importa las bibliotecas necesarias
import streamlit as st
import pandas as pd
import random

# Carga el archivo CSV
@st.cache_data
def load_data():
    return pd.read_csv("Dieta_Keto.csv")

data = load_data()

# Función para seleccionar un alimento al azar de cada columna
def generate_menu():
    desayuno = random.choice(data['Desayunos'].dropna().tolist())
    comida = random.choice(data['Comidas'].dropna().tolist())
    cena = random.choice(data['Cenas'].dropna().tolist())
    return desayuno, comida, cena

# Título de la aplicación
st.title("Generador de Menú Keto para los wawinos")

# Botón para generar el menú
if st.button("Generar menú"):
    desayuno, comida, cena = generate_menu()
    st.write(f"**Desayuno:** {desayuno}")
    st.write(f"**Comida:** {comida}")
    st.write(f"**Cena:** {cena}")
