import streamlit as st
import langchain_helper

st.title('Beauty Store generator')

product = st.sidebar.selectbox("Pick a product", ("Lipstick", "Eyeliner", "Foundation", "Highliter", "Bronzer"))

if(product):
    response = langchain_helper.generate_chemicals_used_in_product(product)
    st.header(response['store_name'])
    chemicals = (response['chemical_name'].strip().split(","))
    st.write("Chemicals used in ",product )
    for chemical in chemicals:
        st.write("-",chemical)


