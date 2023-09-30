import streamlit as st
st.title('My Parents new Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & blueberry Oatmeal')
st.text('🥗 Kale, Spinac & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-range Egg')
st.text('🥑🍞 Avocoado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruit_select=st.multiselect("Pick some fruits:", list(my_fruit_list.index))
st.write(fruit_select)
#dispay the table on page
st.dataframe(my_fruit_list)
