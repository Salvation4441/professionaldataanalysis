import streamlit as st
import os
import time
from numerize.numerize import numerize
from classes.helper import country_salary, ten_country

# to have a wide space
st.set_page_config(page_title='Dashboard', layout='wide', initial_sidebar_state='expanded', )

total_impressions = float(100000000000000)
country_salaryf, country_salaryr = country_salary()

# link css
css_path = os.path.join('static', 'style.css')
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title('🏡:blue[DASHBOARD]')
st.subheader('Data Professional Survey : The  Countries with the Highest Salary')

total1, total2, total3, total4, total5 = st.columns(5, gap='large')

with total1:
    st.image('images/united-arab-emirates.png',width=100, use_column_width='Auto')
    st.metric(label=country_salaryr[0][0], value=f'${numerize(country_salaryr[0][1])}')

with total2:
    st.image('images/denmark.png',width=100, use_column_width='Auto')
    st.metric(label=country_salaryr[1][0], value=f'${numerize(country_salaryr[1][1])}')

with total3:
    st.image('images/ireland.png',width=100, use_column_width='Auto')
    st.metric(label=country_salaryr[2][0], value=f'${numerize(country_salaryr[2][1])}')

with total4:
    st.image('images/united-states.png',width=100, use_column_width='Auto')
    st.metric(label=country_salaryr[3][0], value=f'${numerize(country_salaryr[3][1])}')

with total5:
    st.image('images/australia.png',width=100, use_column_width='Auto')
    st.metric(label=country_salaryr[4][0], value=f'${numerize(country_salaryr[4][1])}')

st.empty()
st.empty()


with st.spinner("Loading..."):
    time.sleep(3)
    st.plotly_chart(country_salaryf,use_container_width=True)

