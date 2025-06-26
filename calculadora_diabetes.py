import streamlit as st

st.title("🩺 Calculadora de Riesgo de Diabetes Tipo 2")

st.write("Responde las siguientes preguntas para estimar tu riesgo:")

edad = st.number_input("¿Cuál es tu edad?", min_value=0, max_value=120)
peso = st.number_input("¿Cuál es tu peso en kg?", min_value=0.0)
altura = st.number_input("¿Cuál es tu altura en metros?", min_value=0.0)
actividad = st.radio("¿Haces actividad física regularmente?", ["Sí", "No"])
familia = st.radio("¿Tienes familiares con diabetes tipo 2?", ["Sí", "No"])

if st.button("Calcular riesgo"):
    if altura == 0:
        st.error("La altura no puede ser 0")
    else:
        imc = peso / (altura ** 2)
        riesgo = 0

        if edad >= 45:
            riesgo += 1
        if imc >= 25:
            riesgo += 1
        if actividad == "No":
            riesgo += 1
        if familia == "Sí":
            riesgo += 1

        st.write(f"Tu IMC es: **{round(imc, 2)}**")

        if riesgo == 0:
            st.success("Riesgo bajo de diabetes tipo 2 🟢")
        elif riesgo <= 2:
            st.warning("Riesgo moderado de diabetes tipo 2 🟡")
        else:
            st.error("Riesgo alto de diabetes tipo 2 🔴")
