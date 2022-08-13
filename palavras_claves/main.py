import streamlit as st
import gateway

def header():
    st.header('Extractor de palavras claves')
    st.markdown("##### ")
    st.text('version 0 - Last update 13/08/2022')

def instert_text():
    txt = st.text_area("Escríba aqui",height=250)
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Extrair"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_palavras_clave(txt)
            
            if status == 200:
                st.text_area(label="WIP", value=new_txt["keywords_and_keyphrases"])
                st.success("¡Está hecho!!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Extractor de palavras claves ❄️")
header()
instert_text()