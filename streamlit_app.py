import streamlit as st
from openai import OpenAI  # yoki Grok API uchun xai SDK

st.title("Mening AI yordamchim")

# API kalitingizni qo‘ying
client = OpenAI(api_key="sizning_kalitingiz")

user_input = st.text_input("Savolingizni yozing:")
if st.button("Yuborish"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # yoki "grok-beta"
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message.content)
