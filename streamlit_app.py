import streamlit
import pandas

streamlit.title('La nueva comida sana de mis padres')
streamlit.header('Desayuno')
streamlit.text('🥣 Leche con cereales')
streamlit.text(' 🥑🍞Pan con sobrasada')
streamlit.text('🥗 🐔Lechuga cual Gallina')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
