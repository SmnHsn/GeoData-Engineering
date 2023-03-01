import streamlit as st

st.sidebar.selectbox(
    'Soil type to analyse',
    ('Clay', 'Sand', 'Limestone'),
                     )

st.sidebar.selectbox(
    'Geotechnical parameter to analyse',
    ('Em', 'Pl*'),
                     )

st.sidebar.checkbox('Using the log of the parameter?')
