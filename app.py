import streamlit as st
import fitz
from PIL import Image
from textwrap3 import wrap
import fitz



st.title('MCQ GENERATOR')
st.subheader('LOAD Pdf:')



uploaded_pdf = st.file_uploader( "       ",type=['pdf'])

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    st.write(text) 
    doc.close()
    if st.button('Generate question'):
     st.write('here it is')
    
    
    
    
    
    
