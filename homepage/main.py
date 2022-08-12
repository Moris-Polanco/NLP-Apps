import streamlit as st
def main_page():
    st.markdown("# Herramientas de IA 🎈")
    st.markdown("## Herramientas de IA para el escritor y el corrector")
    st.markdown("Esta página contiene enlaces a herramientas de procesamiento de lenguaje natural construidas con motores de inteligencia artificial. Para acceder se requiere suscripción. El uso de todas las herramientas es ilimitado para los suscriptores activos, y no se necesita proporcionar ninguna llave de openai u otro proveedor. (Nota: la suscripción no funciona con el navegador Safari.)")
    st.markdown("Al corrector de textos se le recomienda el “Corrector de estilo en español” y el “Acortador”.")
    st.markdown("El escritor puede inspirarse con el “Antibloqueo” o con “Escritor”. Puede seguir este procedimiento:")
    st.markdown("1. Toma un párrafo que él haya escrito y lo somete al corrector de estilo.")
    st.markdown("2. Toma el párrafo corregido y extrae las palabras clave.")
    st.markdown("3. Esas palabras clave las copia en “Estilo Tamaro”.")
    st.markdown("4. Compara su escrito original con el producido por “Estilo Tamaro”.")
    st.markdown("Si le interesa aprender a escribir como determinado autor, solicite la aplicación.")
    st.sidebar.markdown("### Elija las aplicaciones anteriores")

main_page()