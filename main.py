import langchain_helper as lch
import streamlit as st

st.title("🐶🐱 Pets Name Generator 🐹🐮")

user_animal_type = st.sidebar.selectbox("Select your pet:", ("🐱 Cat", "🐶 Dog", "🐮 Cow", "🐹 Hamster"))

pet_color = ""

if user_animal_type:
    pet_color = st.sidebar.text_area(f"Enter the color of your {user_animal_type.split()[1]}:", max_chars=10)

if st.sidebar.button("🚀 Generate Pet Name"):
    if pet_color:
        response = lch.generate_pet_name(user_animal_type.split()[1], pet_color)
        st.write("🐾 Pet Name: " + response['pet_name'])
