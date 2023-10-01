import streamlit as st
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError

#create a function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  frutiyvice_normalized =pd.json_normalize(fruityvice_response.json())
  return frutiyvice_normalized
  
st.title('My Parents new Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & blueberry Oatmeal')
st.text('🥗 Kale, Spinac & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-range Egg')
st.text('🥑🍞 Avocoado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruit_select=st.multiselect("Pick some fruits:", list(my_fruit_list.index))
if len(fruit_select)>0:
  fruits_to_show=my_fruit_list.loc[fruit_select]
  #st.write(fruit_select)
  #dispay the table on page
  st.dataframe(fruits_to_show)
else:
  st.dataframe(my_fruit_list)

#New Section to display druityvice api response
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice=st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.write('Please Select a Fruit to get information.')
  else:
    
    
    # st.write('The user Entered',fruit_choice)
    st.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  st.error()

#st.text(fruityvice_response.json())
#take the json version of the response and normalize it

#output it the screen as a table
# st.dataframe(frutiyvice_normalized)


# my_cnx =snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur=my_cnx.cursor()
st.stop()
# my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST;")
# my_data_row=my_cur.fetchall()
st.header("The fruit load list contains:")
#snowflake related functions

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST;")
    return my_cur.fetchall()
    
if st.button('Get Fruit Load List'):
  my_cnx =snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  st.dataframe(my_data_rows)
add_my_fruit=st.text_input('What fruit would you like to add?')
st.write(f'Thanks for adding {add_my_fruit}')
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit');")
