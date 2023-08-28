import streamlit
import pandas

streamlit.title('La nueva comida sana de mis padres')
streamlit.header('Desayuno')
streamlit.text('🥣 Leche con cereales')
streamlit.text(' 🥑🍞Pan con sobrasada')
streamlit.text('🥗 🐔Lechuga cual Gallina')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
