import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Organizador del Hogar - Finanzas", layout="centered")
st.title("🏠 Organizador Financiero del Hogar")
st.write("Introduce los gastos fijos de tu hogar para calcular recomendaciones de presupuesto de ocio, comida, gasolina y fondo de emergencias.")

# Función principal
def main():
    with st.form("datos_hogar"):
        st.header("Datos del Hogar")
        ingreso = st.number_input("Ingresos totales del hogar (€):", min_value=0.0, step=50.0, format="%.2f")
        num_personas = st.number_input("Número de personas en el hogar:", min_value=1, step=1)
        num_vehiculos = st.number_input("Número de vehículos:", min_value=0, step=1)

        # Tipos de vehículos dinámicos
        tipos_vehiculos = []
        if num_vehiculos > 0:
            st.subheader("Tipo de vehículo por unidad")
            opciones = ["Coche pequeño", "Coche medio", "SUV/4x4"]
            for i in range(num_vehiculos):
                tipo = st.selectbox(
                    f"Tipo de vehículo {i+1}",
                    opciones,
                    key=f"tipo_vehiculo_{i}"
                )
                tipos_vehiculos.append(tipo)

        st.subheader("Gastos fijos mensuales (€)")
        hipoteca = st.number_input("Hipoteca / Alquiler:", min_value=0.0, step=10.0, format="%.2f")
        agua = st.number_input("Agua:", min_value=0.0, step=5.0, format="%.2f")
        luz = st.number_input("Luz:", min_value=0.0, step=5.0, format="%.2f")
        gas = st.number_input("Gas (natural/calefacción):", min_value=0.0, step=5.0, format="%.2f")
        internet_movil = st.number_input("Internet y móvil:", min_value=0.0, step=5.0, format="%.2f")
        deudas = st.number_input("Deudas pendientes:", min_value=0.0, step=10.0, format="%.2f")
        seguros = st.number_input("Seguros contratados:", min_value=0.0, step=10.0, format="%.2f")
        otros_fijos = st.number_input("Otros gastos fijos:", min_value=0.0, step=10.0, format="%.2f")

        submitted = st.form_submit_button("Calcular")

    if submitted:
        # Cálculo de totales
        total_fijos = hipoteca + agua + luz + gas + internet_movil + deudas + seguros + otros_fijos
        sobrante = ingreso - total_fijos

        # Recomendaciones profesionales
        comida = round(num_personas * 120, 2)
        # Map de precio mensual por tipo de vehículo
        gas_price_map = {
            "Coche pequeño": 80,
            "Coche medio": 120,
            "SUV/4x4": 160
        }
        gasolina = round(sum(gas_price_map.get(t, 0) for t in tipos_vehiculos), 2)
        fondo_emergencias = round(sobrante * 0.10, 2)
        ocio = round(sobrante * 0.10, 2)

        # Saldo restante después de asignaciones
        asignado = comida + gasolina + fondo_emergencias + ocio
        saldo_restante = round(sobrante - asignado, 2)

        # Presentación de resultados
        st.header("📋 Resultados y Recomendaciones")
        st.write(f"**Ingresos totales:** €{ingreso:.2f}")
        st.write(f"**Gastos fijos totales:** €{total_fijos:.2f}")
        st.write(f"**Sobrante después de gastos fijos:** €{sobrante:.2f}")
        st.markdown("---")

        # Métricas detalladas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("🍽️ Comida")
            st.metric(label="Budget (€)", value=f"€{comida}")
        with col2:
            st.subheader("⛽ Gasolina")
            st.metric(label="Budget (€)", value=f"€{gasolina}")
        with col3:
            st.subheader("🎉 Ocio")
            st.metric(label="Budget (€)", value=f"€{ocio}")

        col4, col5 = st.columns(2)
        with col4:
            st.subheader("🛠️ Fondo Emergencias")
            st.metric(label="Budget (€)", value=f"€{fondo_emergencias}")
        with col5:
            st.subheader("💼 Saldo Restante")
            if saldo_restante < 0:
                st.error(f"Déficit de €{abs(saldo_restante):.2f} - ajusta tus gastos.")
            else:
                st.metric(label="Saldo (€)", value=f"€{saldo_restante}")

        # Consejos finales
        st.markdown("---")
        st.subheader("Consejos Profesionales 🔍")
        st.write(
            "- Revisa tus gastos fijos periódicamente.\n"
            "- Ajusta las recomendaciones según tu estilo de vida.\n"
            "- Reserva un porcentaje extra si prevés imprevistos."
        )

if __name__ == "__main__":
    main()
     