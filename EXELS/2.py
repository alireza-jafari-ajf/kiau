import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)

local_css("style/style.css")



symbol_animation = "❄️"
st.markdown(f"""
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
<div class="snowflake">{symbol_animation}</div>
""" , unsafe_allow_html=True)