import streamlit as st

# Título de la aplicación
st.set_page_config(page_title="Gestor Personal de Finanzas", layout="centered")
st.title("📊 Gestor Personal de Finanzas")
st.write("Introduce tus ingresos y gastos fijos para calcular tu presupuesto de ocio y ahorro.")

# Formulario de entrada
with st.form("datos_financieros"):
    st.header("Datos mensuales")
    ingreso = st.number_input("Ingresos mensuales (€):", min_value=0.0, step=50.0, format="%.2f")
    st.subheader("Gastos fijos mensuales (€)")
    hipoteca = st.number_input("Hipoteca / Alquiler:", min_value=0.0, step=10.0, format="%.2f")
    agua = st.number_input("Agua:", min_value=0.0, step=5.0, format="%.2f")
    luz = st.number_input("Luz:", min_value=0.0, step=5.0, format="%.2f")
    gas = st.number_input("Gas:", min_value=0.0, step=5.0, format="%.2f")
    internet = st.number_input("Internet y teléfono:", min_value=0.0, step=5.0, format="%.2f")
    otros = st.number_input("Otros gastos fijos:", min_value=0.0, step=10.0, format="%.2f")
    submitted = st.form_submit_button("Siguiente")

# Procesamiento y resultados
if submitted:
    total_gastos_fijos = hipoteca + agua + luz + gas + internet + otros
    sobrante = ingreso - total_gastos_fijos
    # Regla profesional: 20% de ahorro del ingreso total
    ahorro_recomendado = round(ingreso * 0.20, 2)
    # Presupuesto para ocio y otros = sobrante - ahorro
    ocio_presupuesto = round(sobrante - ahorro_recomendado, 2)

    st.header("📝 Resultados mensuales")
    st.write(f"**Ingresos mensuales:** €{ingreso:.2f}")
    st.write(f"**Gastos fijos totales:** €{total_gastos_fijos:.2f}")
    st.write(f"**Sobrante después de gastos fijos:** €{sobrante:.2f}")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💰 Ahorro recomendado (20%)")
        st.metric(label="Ahorro (€)", value=f"€{ahorro_recomendado}")
    with col2:
        st.subheader("🎉 Presupuesto ocio y otros")
        if ocio_presupuesto < 0:
            st.error(f"No es posible asignar presupuesto de ocio. Déficit de €{abs(ocio_presupuesto):.2f}")
        else:
            st.metric(label="Ocio (€)", value=f"€{ocio_presupuesto}")

    # Consejos adicionales
    st.markdown("---")
    st.subheader("Consejos profesionales 🔍")
    st.write(
        "- Trata de mantener tus gastos fijos por debajo del 50% de tus ingresos.\n"
        "- Ajusta tus ahorros si necesitas reforzar tu fondo de emergencia.\n"
        "- Revisa tus gastos variables cada mes para optimizar tu presupuesto."
    )

# Pie de página
st.sidebar.write("© 2025 Gestor Personal de Finanzas")
