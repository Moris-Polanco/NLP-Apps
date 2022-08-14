import streamlit as st
import gateway

def header():
    st.header('Estilo Tamara')
    st.markdown("##### Aprenda a escribir al estilo de Donde el corazón te lleve, de Susana Tamaro.")
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Ingrese 6-12 palavras clave, separadas por coma y com punto al final.")
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Genere Texto"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_estilo_tamara(txt)
            status = 200
            
            if status == 200:
                st.text_area(label="Estilo Tamara :", value=new_txt, height=250)
                st.success("Sucess!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpiar"):
        st.info("cleaning")

st.sidebar.markdown("# Estilo Tamara ❄️")
header()
instert_text()