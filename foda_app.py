import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Simulador FODA - Pollería Koky's", layout="wide")
st.title("🚀 Simulador FODA para Pollería Koky's")

# Logo ASCII de Koky's
st.code("""
   ____          _          
  / __ \\        (_)         
 | |  | | __ _   _ _ __   ___ 
 | |  | |/ _` | | | '_ \\ / __|
 | |__| | (_| | | | | | | (__)
  \\____/ \\__,_|_|_|_| |_|___|
    Pollería Koky's - ¡Sabor que enamora!
""", language='')

# Introducción
st.markdown("**Rol: Gerente General** - Deduce los elementos FODA, clasifícalos y define estrategias para Koky's.")

# Descripción de la empresa
st.header("Descripción de Pollería Koky's")
st.write("""
Pollería Koky's es una cadena de restaurantes con 10 locales en Lima, Perú. Fundada hace 15 años, es conocida por su sabor tradicional y ambiente familiar. """)

# Objetivos estratégicos
st.header("Objetivos Estratégicos de Koky's")
st.write("""
1. **Aumentar las ventas en un 20%** en los próximos 12 meses.
2. **Mejorar la experiencia del cliente** mediante modernización y digitalización.
3. **Reducir costos operativos en un 10%** optimizando procesos.
4. **Fortalecer la presencia de marca** a través de marketing y alianzas.
""")

# Instrucciones
st.header("Instrucciones")
st.write("1. Clasifica los 16 elementos en la matriz FODA.")
st.write("2. Revisa estrategias cruzadas y selecciona al menos 3.")
st.write("3. Justifica tu selección considerando costo, tiempo y objetivos.")

# Elementos para clasificar
elements = [
    "Receta tradicional de pollo a la brasa que atrae clientes recurrentes",
    "Escasa presencia en redes sociales y campañas publicitarias",
    "Creciente demanda de pedidos a través de plataformas digitales",
    "Competencia intensa de cadenas nacionales e internacionales",
    "Equipo con experiencia en atención al cliente y preparación de alimentos",
    "Dependencia de proveedores locales para insumos clave",
    "Posibilidad de abrir locales en distritos emergentes de Lima",
    "Incremento en precios de insumos y energía",
    "Locales en zonas de alto tráfico con fácil acceso",
    "Algunos locales requieren renovación para mejorar la experiencia",
    "Interés en opciones bajas en grasa o acompañamientos saludables",
    "Normas sanitarias más estrictas que exigen mayores inversiones",
    "Sólida reputación en Lima por calidad y servicio",
    "Falta de un sistema robusto de pedidos en línea",
    "Oportunidad de alianzas con apps de delivery",
    "Clientes buscan experiencias gastronómicas innovadoras"
]

# Mapeo de categorías
plural_map = {
    "Fortaleza": "Fortalezas",
    "Debilidad": "Debilidades",
    "Oportunidad": "Oportunidades",
    "Amenaza": "Amenazas"
}

# Inicializar session_state
if 'foda_classification' not in st.session_state:
    st.session_state.foda_classification = {
        "Fortalezas": [],
        "Debilidades": [],
        "Oportunidades": [],
        "Amenazas": []
    }
if 'valid' not in st.session_state:
    st.session_state.valid = False
if 'selected_strategies' not in st.session_state:
    st.session_state.selected_strategies = []
if 'justification' not in st.session_state:
    st.session_state.justification = ""

# --- SECCIÓN DE CLASIFICACIÓN FODA ---
with st.form("foda_form"):
    st.header("🧩 Clasifica los Elementos FODA")
    selected_categories = {}
    for element in elements:
        category = st.selectbox(f"Clasifica: {element}", ["Selecciona","Fortaleza", "Debilidad", "Oportunidad", "Amenaza"], key=element)
        selected_categories[element] = category
    if st.form_submit_button("Evaluar Matriz FODA"):  # ✅ Botón añadido
        st.session_state.foda_classification = {
            "Fortalezas": [],
            "Debilidades": [],
            "Oportunidades": [],
            "Amenazas": []
        }
        for element, cat in selected_categories.items():
            plural = plural_map[cat]
            st.session_state.foda_classification[plural].append(element)

        valid = all(len(st.session_state.foda_classification[cat]) == 4 for cat in st.session_state.foda_classification)
        st.session_state.valid = valid
        if not valid:
            st.error("Error: Asegúrate de que cada categoría tenga exactamente 4 elementos.")

# Mostrar resultados si válido
if st.session_state.valid:
    st.success("✅ ¡Matriz FODA clasificada correctamente!")

    # Mostrar FODA
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Factores Internos")
        st.write("**Fortalezas:**")
        for i, f in enumerate(st.session_state.foda_classification["Fortalezas"], 1):
            st.write(f"{i}. {f}")
        st.write("**Debilidades:**")
        for i, d in enumerate(st.session_state.foda_classification["Debilidades"], 1):
            st.write(f"{i}. {d}")
    with col2:
        st.subheader("Factores Externos")
        st.write("**Oportunidades:**")
        for i, o in enumerate(st.session_state.foda_classification["Oportunidades"], 1):
            st.write(f"{i}. {o}")
        st.write("**Amenazas:**")
        for i, a in enumerate(st.session_state.foda_classification["Amenazas"], 1):
            st.write(f"{i}. {a}")

    # Definir estrategias
    fo_strategies = [
        {"estrategia": "Implementar un sistema de pedidos en línea propio", "costo": 50000, "tiempo": 6, "objetivos": [1, 2], "impacto": "Aumenta ventas por delivery"},
        {"estrategia": "Lanzar menú saludable", "costo": 30000, "tiempo": 4, "objetivos": [1, 4], "impacto": "Captura nuevos segmentos"},
        {"estrategia": "Expandir a distritos emergentes", "costo": 120000, "tiempo": 9, "objetivos": [1, 4], "impacto": "Amplía base de clientes"}
    ]
    fa_strategies = [
        {"estrategia": "Reforzar lealtad con clientes recurrentes", "costo": 8000, "tiempo": 2, "objetivos": [1, 4], "impacto": "Retiene clientes frecuentes"},
        {"estrategia": "Capacitar equipo en nuevas técnicas", "costo": 15000, "tiempo": 3, "objetivos": [2, 3], "impacto": "Mejora eficiencia"}
    ]
    do_strategies = [
        {"estrategia": "Invertir en marketing digital", "costo": 30000, "tiempo": 6, "objetivos": [1, 4], "impacto": "Mejora visibilidad"},
        {"estrategia": "Alianzas con apps de delivery", "costo": 40000, "tiempo": 5, "objetivos": [1, 2], "impacto": "Incrementa ventas"}
    ]
    da_strategies = [
        {"estrategia": "Modernizar locales con diseño temático", "costo": 80000, "tiempo": 8, "objetivos": [2, 3], "impacto": "Mejora experiencia y reduce costos"},
        {"estrategia": "Sistema de gestión energética", "costo": 25000, "tiempo": 4, "objetivos": [3], "impacto": "Reduce gastos"}
    ]

    # Convertir a DataFrames
    fo_df = pd.DataFrame(fo_strategies)
    fa_df = pd.DataFrame(fa_strategies)
    do_df = pd.DataFrame(do_strategies)
    da_df = pd.DataFrame(da_strategies)

    # Tabs para ver estrategias
    tabs = st.tabs(["FO", "FA", "DO", "DA"])
    with tabs[0]: st.dataframe(fo_df)
    with tabs[1]: st.dataframe(fa_df)
    with tabs[2]: st.dataframe(do_df)
    with tabs[3]: st.dataframe(da_df)

    # Selección de estrategias
    with st.form("strategy_form"):
        st.header("🔍 Selecciona tus Estrategias")
        st.info("Elige al menos 3 estrategias y justifica tu elección.")

        selected_strategies = []
        scores = []

        strategies_list = [
            ("FO", fo_df), ("FA", fa_df), ("DO", do_df), ("DA", da_df)
        ]

        for strategy_type, df in strategies_list:
            st.subheader(f"Estrategias {strategy_type}")
            for i, row in df.iterrows():
                if st.checkbox(
                    f"{row['estrategia']} (Costo: S/{row['costo']}, Tiempo: {row['tiempo']} meses)",
                    key=f"{strategy_type}_{i}"
                ):
                    selected_strategies.append(row)
                    score = max(0, 100 - row['costo']/2000) + max(0, 100 - row['tiempo']*5) + len(row['objetivos']) * 10
                    scores.append({"estrategia": row['estrategia'], "puntuación": round(score, 2)})

        justification = st.text_area("Justifica tu selección considerando costo, tiempo y objetivos:")

        if st.form_submit_button("Confirmar Selección"):  # ✅ Botón agregado
            if len(selected_strategies) >= 3 and justification.strip():
                st.session_state.selected_strategies = selected_strategies
                st.session_state.justification = justification
                st.rerun()
            else:
                st.warning("Por favor, selecciona al menos 3 estrategias y proporciona una justificación válida.")

# Resultados finales
if st.session_state.selected_strategies:
    st.success("✅ Estrategias seleccionadas exitosamente!")
    selected_strategies = st.session_state.selected_strategies
    total_cost = sum(s['costo'] for s in selected_strategies)
    total_time = sum(s['tiempo'] for s in selected_strategies)
    avg_score = sum(s["puntuación"] for s in scores) / len(scores)

    st.write(f"💰 Costo Total: S/{total_cost}")
    st.write(f"⏱️ Tiempo Total: {total_time} meses")
    st.write(f"📊 Puntaje Promedio: {round(avg_score, 2)}/200")

    for i, strat in enumerate(selected_strategies, 1):
        st.markdown(f"**{i}. {strat['estrategia']}**")
        st.write(f"- Costo: S/{strat['costo']}")
        st.write(f"- Tiempo: {strat['tiempo']} meses")
        st.write(f"- Impacto: {strat['impacto']}")
        st.write(f"- Objetivos: {strat['objetivos']}")
        st.write("---")

    st.markdown("### 📝 Justificación")
    st.write(st.session_state.justification)

    if avg_score > 150:
        st.success("🌟 Excelente elección. Estrategias bien balanceadas.")
    elif avg_score > 100:
        st.info("✔ Buena elección, pero revisa posibles ajustes.")
    else:
        st.warning("🛠 Mejora tu selección. Prioriza bajo costo y alto impacto.")

# Nota final
st.markdown("---")
st.write("🧠 Desarrollado por Wilton Torvisco para fines educativos.")
