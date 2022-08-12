import streamlit as st
import gateways

def header():
    st.header('Parafraseador')
    st.markdown("##### Cambia las palabras de un texto, manteniendo el significado y sentido.")
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Escríba aqui",height=250)
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Acortar"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateways.conect_parafraseor(txt)
            
            if status == 200:
                st.text_area(label="Texto parafraseado:", value=new_txt["paraphrased_text"])
                st.success("¡Está hecho!!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Parafraseador ❄️")
header()
instert_text()