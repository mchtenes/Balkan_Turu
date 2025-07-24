import streamlit as st
import streamlit.components.v1 as components

# Başlık
st.set_page_config(layout="wide")
st.title("🗺️ Balkan Turu Haritası")

# HTML dosyasını oku
with open("balkan_turu.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# HTML içeriğini göster
components.html(html_content, height=800, scrolling=True)
