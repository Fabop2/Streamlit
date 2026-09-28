import streamlit as st
import joblib
import pandas as pd

# Configuración de la página

st.set_page_config(
page_title="Predicción de Ataque Pokémon",
page_icon="⚡",
layout="centered"
)

# Cargar modelo

modelo = joblib.load("modelo_ataque_pokemon(1).pkl")

# Título

st.title("⚡ Predictor de Ataque Pokémon")
st.write(
"Ingresa las estadísticas de un Pokémon para estimar su valor de **Attack**."
)

# Entradas del usuario

st.subheader("Estadísticas del Pokémon")

hp = st.number_input(
"HP",
min_value=1.0,
max_value=300.0,
value=70.0,
step=1.0
)

defense = st.number_input(
"Defense",
min_value=1.0,
max_value=300.0,
value=70.0,
step=1.0
)

sp_atk = st.number_input(
"Sp. Atk",
min_value=1.0,
max_value=300.0,
value=70.0,
step=1.0
)

sp_def = st.number_input(
"Sp. Def",
min_value=1.0,
max_value=300.0,
value=70.0,
step=1.0
)

speed = st.number_input(
"Speed",
min_value=1.0,
max_value=300.0,
value=70.0,
step=1.0
)
# Botón de predicción
if st.button("Predecir Attack"):

    datos = pd.DataFrame({
        "HP": [hp],
        "Defense": [defense],
        "Sp. Atk": [sp_atk],
        "Sp. Def": [sp_def],
        "Speed": [speed]
    })

    prediccion = modelo.predict(datos)[0]

    st.success(f"⚔️ Attack estimado: {prediccion:.2f}")

    st.write("### Datos ingresados")
    st.dataframe(datos)
