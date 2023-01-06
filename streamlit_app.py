import streamlit
import pandas as pd

streamlit.title('Streamlit\'s Newly Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import dataframe from S3 and set index to fruit
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# display multiselect referencing my_fruit_list index
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado,'Strawberries'])

# show dataframe
streamlit.dataframe(my_fruit_list)
