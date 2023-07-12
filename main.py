import streamlit as st

st.title('Restaurant name generator')

st.sidebar.selectbox('pick a restaurant', ('arabian', 'mexican', 'indian', 'spanish',
                                        'italian','pakistani', 'iranian', 'american', 'british', 'african'))