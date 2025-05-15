import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestor Personal de Finanzas", layout="centered")
st.title("📊 Gestor Personal de Finanzas")
st.write("Introduce tus ingresos y gastos para calcular tu presupuesto de ocio, ahorro y otros gastos variables.")

# Formulario de entrada
with st.form("datos_financieros"):
    st.header("Datos mensuales")
    ingreso = st.number_input("Ingresos mensuales (€):", min_value=0.0, step=50.0, format="%.2f")

    st.subheader("Gastos fijos mensuales (€)")
    hipoteca = st.number_input("Hipoteca / Alquiler:", min_value=0.0, step=10.0, format="%.2f")
    agua = st.number_input("Agua:", min_value=0.0, step=5.0, format="%.2f")
    luz = st.number_input("Luz:", min_value=0.0, step=5.0, format="%.2f")
    gas = st.number_input("Gas (calefacción/gas):", min_value=0.0, step=5.0, format="%.2f")
    internet = st.number_input("Internet y teléfono:", min_value=0.0, step=5.0, format="%.2f")
    otros_fijos = st.number_input("Otros gastos fijos:", min_value=0.0, step=10.0, format="%.2f")

    st.subheader("Gastos variables")
    compras_semanales = st.number_input("Compras semanales (€):", min_value=0.0, step=5.0, format="%.2f")
    gasolina = st.number_input("Gasolina mensual (€):", min_value=0.0, step=5.0, format="%.2f")
    otros_variables = st.number_input("Otros gastos variables mensuales (€):", min_value=0.0, step=10.0, format="%.2f")

    submitted = st.form_submit_button("Siguiente")

# Cálculo y resultados
if submitted:
    total_gastos_fijos = hipoteca + agua + luz + gas + internet + otros_fijos
    # Convierto compras semanales a gasto mensual aproximado (x4)
    total_compras = compras_semanales * 4
    total_gastos_variables = total_compras + gasolina + otros_variables

    sobrante = ingreso - total_gastos_fijos - total_gastos_variables
    # Recomendación de ahorro: 20% de los ingresos
    ahorro_recomendado = round(ingreso * 0.20, 2)
    ocio_presupuesto = round(sobrante - ahorro_recomendado, 2)

    st.header("📝 Resultados mensuales")
    st.write(f"**Ingresos mensuales:** €{ingreso:.2f}")
    st.write(f"**Gastos fijos totales:** €{total_gastos_fijos:.2f}")
    st.write(f"**Gastos variables totales:** €{total_gastos_variables:.2f}")
    st.write(f"**Sobrante después de gastos:** €{sobrante:.2f}")
    st.markdown("---")

    # Métricas detalladas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("💰 Ahorro recomendado (20%)")
        st.metric("Ahorro (€)", f"€{ahorro_recomendado}")
    with col2:
        st.subheader("🛒 Compras mensuales")
        st.metric("Compras (€)", f"€{total_compras:.2f}")
    with col3:
        st.subheader("⛽ Gasolina")
        st.metric("Gasolina (€)", f"€{gasolina:.2f}")

    st.markdown("---")
    st.subheader("🎉 Presupuesto ocio y otros")
    if ocio_presupuesto < 0:
        st.error(f"No es posible asignar presupuesto de ocio. Déficit de €{abs(ocio_presupuesto):.2f}")
    else:
        st.metric("Ocio (€)", f"€{ocio_presupuesto}")

    # Consejos profesionales
    st.markdown("---")
    st.subheader("Consejos profesionales 🔍")
    st.write(
        "- Mantén tus gastos fijos por debajo del 50% de tus ingresos.\n"
        "- Ajusta tu porcentaje de ahorro si necesitas reforzar tu fondo de emergencia.\n"
        "- Revisa y optimiza tus gastos variables mensualmente."
    )

# Pie de página
st.sidebar.write("© 2025 Gestor Personal de Finanzas")
