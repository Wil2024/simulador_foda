import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Simulador FODA - Pollería Koky's", layout="wide")
st.title("Simulador FODA para Pollería Koky's")

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

st.markdown("**Rol: Gerente General** - Deduce los elementos FODA, clasifícalos y define estrategias para Koky's.")

# Descripción de la empresa
st.header("Descripción de Pollería Koky's")
st.write("""
Pollería Koky's es una cadena de restaurantes con 10 locales en Lima, Perú, especializada en pollo a la brasa y comida criolla. Fundada hace 15 años, es conocida por su sabor tradicional y ambiente familiar. A continuación, se presentan características y contexto de la empresa (tú decides si cada elemento es una fortaleza, debilidad, oportunidad o amenaza):
- Receta tradicional de pollo a la brasa que atrae clientes recurrentes.
- Escasa presencia en redes sociales y campañas publicitarias.
- Creciente demanda de pedidos a través de plataformas digitales.
- Competencia intensa de cadenas nacionales e internacionales (Norky's, KFC).
- Equipo con experiencia en atención al cliente y preparación de alimentos.
- Dependencia de proveedores locales para insumos clave.
- Posibilidad de abrir locales en distritos emergentes de Lima.
- Incremento en precios de insumos y energía.
- Locales en zonas de alto tráfico con fácil acceso.
- Algunos locales requieren renovación para mejorar la experiencia.
- Interés en opciones bajas en grasa o acompañamientos saludables.
- Normas sanitarias más estrictas que exigen mayores inversiones.
- Sólida reputación en Lima por calidad y servicio.
- Falta de un sistema robusto de pedidos en línea.
- Oportunidad de alianzas con apps de delivery (Rappi, PedidosYa).
- Clientes buscan experiencias gastronómicas innovadoras.
""")

# Objetivos estratégicos
st.header("Objetivos Estratégicos de Koky's")
st.write("""
1. **Aumentar las ventas en un 20%** en los próximos 12 meses.
2. **Mejorar la experiencia del cliente** mediante modernización y digitalización.
3. **Reducir costos operativos en un 10%** optimizando procesos.
4. **Fortalecer la presencia de marca** a través de marketing y alianzas.
""")

# Instrucciones para los estudiantes
st.header("Instrucciones")
st.write("""
1. Lee la descripción de Koky's y deduce si cada elemento es una **fortaleza**, **debilidad**, **oportunidad** o **amenaza**.
2. Clasifica cada uno de los 16 elementos en la matriz FODA usando los menús desplegables. Asegúrate de que cada categoría tenga exactamente 4 elementos.
3. Revisa las estrategias cruzadas sugeridas y selecciona al menos 3 que mejor cumplan los objetivos, considerando **costo** (en soles), **tiempo** (en meses) y alineación con los **objetivos estratégicos**.
4. Justifica tu selección y confirma para recibir retroalimentación y una puntuación.
""")

# Diccionario para mapear singular a plural
plural_map = {
    "Fortaleza": "Fortalezas",
    "Debilidad": "Debilidades",
    "Oportunidad": "Oportunidades",
    "Amenaza": "Amenazas"
}

# Lista de elementos para clasificar
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

# Usar session_state para persistir datos
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
    st.header("Clasifica los Elementos FODA")
    st.write("Selecciona la categoría correspondiente para cada elemento.")
    
    selected_categories = {}
    for element in elements:
        category = st.selectbox(
            f"Clasifica: {element}",
            ["Fortaleza", "Debilidad", "Oportunidad", "Amenaza"],
            key=element
        )
        selected_categories[element] = category
    
    submit = st.form_submit_button("Evaluar Matriz FODA")
    
    if submit:
        # Actualizar clasificación en session_state
        st.session_state.foda_classification = {
            "Fortalezas": [],
            "Debilidades": [],
            "Oportunidades": [],
            "Amenazas": []
        }
        
        for element, cat in selected_categories.items():
            plural = plural_map[cat]
            st.session_state.foda_classification[plural].append(element)
        
        # Validar que cada categoría tenga 4 elementos
        valid = all(len(st.session_state.foda_classification[cat]) == 4 for cat in st.session_state.foda_classification)
        st.session_state.valid = valid  # Almacenar el estado en session_state
        
        if not valid:
            st.error("Error: Asegúrate de que cada categoría tenga **exactamente 4 elementos**.")
            st.stop()

# --- MOSTRAR RESULTADOS SI LA CLASIFICACIÓN ES VÁLIDA ---
if st.session_state.valid:
    st.success("¡Matriz FODA clasificada correctamente!")
    
    # Mostrar matriz FODA
    st.header("Tu Matriz FODA")
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
    
    # Generar estrategias cruzadas
    st.header("Estrategias Cruzadas Recomendadas")
    
    # Estrategias FO
    st.subheader("Estrategias FO (Aprovechar fortalezas para capturar oportunidades)")
    fo_strategies = [
        {"estrategia": "Implementar un sistema de pedidos en línea propio...", "costo": 50000, "tiempo": 6, "objetivos": [1, 2], "impacto": "Aumenta ventas por delivery..."},
        # ... (todos los elementos de FO completos)
    ]
    fo_df = pd.DataFrame(fo_strategies)
    st.dataframe(fo_df)
    
    # Estrategias FA
    st.subheader("Estrategias FA (Usar fortalezas para mitigar amenazas)")
    fa_strategies = [
        {"estrategia": "Reforzar la lealtad de clientes...", "costo": 8000, "tiempo": 2, "objetivos": [1, 4], "impacto": "Retiene clientes..."},
        # ... (todos los elementos de FA completos)
    ]
    fa_df = pd.DataFrame(fa_strategies)
    st.dataframe(fa_df)
    
    # Estrategias DO
    st.subheader("Estrategias DO (Superar debilidades aprovechando oportunidades)")
    do_strategies = [
        {"estrategia": "Invertir en marketing digital...", "costo": 30000, "tiempo": 6, "objetivos": [1, 4], "impacto": "Aumenta visibilidad..."},
        # ... (todos los elementos de DO completos)
    ]
    do_df = pd.DataFrame(do_strategies)
    st.dataframe(do_df)
    
    # Estrategias DA
    st.subheader("Estrategias DA (Minimizar debilidades para enfrentar amenazas)")
    da_strategies = [
        {"estrategia": "Implementar un plan de mantenimiento...", "costo": 40000, "tiempo": 10, "objetivos": [3], "impacto": "Reduce gastos..."},
        # ... (todos los elementos de DA completos)
    ]
    da_df = pd.DataFrame(da_strategies)
    st.dataframe(da_df)
    
    # --- SECCIÓN DE SELECCIÓN DE ESTRATEGIAS ---
    with st.form("strategy_form"):
        st.header("Selecciona tus Estrategias")
        st.write("Elige al menos 3 estrategias que mejor cumplan los objetivos, considerando **costo** (en soles) y **tiempo** (en meses). Recibirás retroalimentación y una puntuación.")
        
        selected_strategies = []
        scores = []
        for strategy_type, df in [("FO", fo_df), ("FA", fa_df), ("DO", do_df), ("DA", da_df)]:
            st.subheader(f"Estrategias {strategy_type}")
            for i, row in df.iterrows():
                if st.checkbox(
                    f"{row['estrategia']} (Costo: S/{row['costo']}, Tiempo: {row['tiempo']} meses, Objetivos: {row['objetivos']})",
                    key=f"{strategy_type}_{i}"
                ):
                    selected_strategies.append(row)
                    # Calcular puntuación
                    cost_score = max(0, 100 - row['costo'] / 2000)
                    time_score = max(0, 100 - row['tiempo'] * 5)
                    obj_score = len(row['objetivos']) * 20
                    total_score = cost_score + time_score + obj_score
                    scores.append({"estrategia": row['estrategia'], "puntuación": round(total_score, 2)})
        
        justification = st.text_area("Justifica tu selección de estrategias (considera costo, tiempo y objetivos):")
        submit_strategy = st.form_submit_button("Confirmar Selección")
        
        
if submit_strategy:
    if len(selected_strategies) >= 3 and justification.strip():
        # Almacenar selección en session_state
        st.session_state.selected_strategies = selected_strategies
        st.session_state.justification = justification
        st.rerun()  # <<--- CAMBIO AQUÍ
    else:
        st.error("Por favor, selecciona al menos 3 estrategias y proporciona una justificación.")

# --- SECCIÓN DE RESULTADOS Y RETROALIMENTACIÓN ---
if st.session_state.selected_strategies:
    st.success("¡Estrategias seleccionadas correctamente!")
    selected_strategies = st.session_state.selected_strategies
    justification = st.session_state.justification
    
    total_score = sum(s["puntuación"] for s in scores) / len(selected_strategies)
    total_costo = sum(s['costo'] for s in selected_strategies)
    total_tiempo = sum(s['tiempo'] for s in selected_strategies)
    
    st.subheader("Estrategias Elegidas")
    for i, strategy in enumerate(selected_strategies, 1):
        st.write(f"{i}. **{strategy['estrategia']}**")
        st.write(f"- Costo: S/{strategy['costo']}")
        st.write(f"- Tiempo: {strategy['tiempo']} meses")
        st.write(f"- **Impacto**: {strategy['impacto']}")
        st.write(f"- **Objetivos cubiertos**: {strategy['objetivos']}")
        # Buscar puntuación
        score = next(s["puntuación"] for s in scores if s["estrategia"] == strategy['estrategia'])
        st.write(f"- **Puntuación**: {score}/300")
        
        # Retroalimentación específica
        if strategy['costo'] > 50000:
            st.warning(f"¡Costo elevado!: La estrategia '{strategy['estrategia']}' requiere un presupuesto mayor.")
        if strategy['tiempo'] > 12:
            st.warning(f"¡Tiempo prolongado!: La estrategia '{strategy['estrategia']}' tarda más de un año.")
        if len(strategy['objetivos']) < 2:
            st.info(f"¡Enfocado!: La estrategia '{strategy['estrategia']}' cubre pocos objetivos.")
    
    st.write(f"**Costo total estimado: S/{total_costo}**")
    st.write(f"**Tiempo total estimado: {total_tiempo} meses**")
    
    st.subheader("Justificación")
    st.write(justification)
    
    st.subheader("Puntuación Total")
    st.write(f"Promedio: {round(total_score, 2)}/300")
    
    if total_score > 200:
        st.success("¡Excelente selección! Las estrategias son viables y bien alineadas.")
    elif total_score > 150:
        st.info("Buena selección, pero revisa el balance entre costo, tiempo y objetivos.")
    else:
        st.warning("Selección mejorable: Prioriza estrategias de menor costo y mayor impacto.")

# --- NOTA FINAL ---
st.markdown("---")
st.write("Desarrollado por Wilton Torvisco utilizando Grok 3 para fines educativos. ¡Buena suerte, Gerente General!")