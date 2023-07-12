import streamlit as st
from helper import name_item_generator

st.title('Restaurant name generator')

cuisine = st.sidebar.selectbox('pick a restaurant', ('arabian', 'mexican', 'indian', 'spanish',
                                        'italian','pakistani', 'iranian', 'american', 'british', 'african'))

if cuisine:
    response = name_item_generator(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')
    st.write('**Menu Items**')
    for menu in menu_items:
        st.write('  -', menu)
