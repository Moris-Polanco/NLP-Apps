import streamlit as st
import gateway

def header():
    st.header('Antibloqueo')
    st.markdown("##### Supere el bloqueo del escritor. ")
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("-")
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Escriba Más"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_antibloqueo(txt)
            status = 200
            
            if status == 200:
                st.text_area(label="Escriba!", value=new_txt, height=250)
                st.success("Sucess!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpiar"):
        st.info("cleaning")

st.sidebar.markdown("# Antibloqueo ❄️")
header()
instert_text()