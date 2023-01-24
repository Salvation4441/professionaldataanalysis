import streamlit as st
import pandas as pd
import os
import time

from classes.helper import gender, age_group, edu, ethnicity, role, industry, programming

st.set_page_config(page_title='Survey', layout='wide', initial_sidebar_state='expanded', )

# link css
css_path = os.path.join('static', 'style.css')
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title('✌️:green[Data Professional Survey]')

with st.expander("Data Professional Survey", expanded=True):
    tabs = ['Gender', 'Age', 'Education', 'Ethnicity', 'Roles', 'Industry','Programming Language']

    tab1, tab2, tab3, tab4, tab5, tab6,tab7= st.tabs(tabs)
    with tab1:
        st.caption('Data Professional Survey on Gender with Average Salary')
        st.plotly_chart(gender(), use_container_width=True)

    with tab2:
        st.caption('Data Professional Survey on Gender with Average Salary', )
        st.plotly_chart(age_group(), use_container_width=True)

    with tab3:
        st.caption('Data Professional Survey Average Salary vs Highest Level of Education')
        st.plotly_chart(edu(), use_container_width=True)

    with tab4:
        st.caption('Data Professional Survey: Ethnicity vrs Average Salary')
        st.plotly_chart(ethnicity(), use_container_width=True)

    with tab5:
         st.caption('Job roles with number of respondents present for that job')
         st.plotly_chart(role(),use_container_width=True)

    with tab6:
        st.caption('Percentage Change in Sales')
        st.plotly_chart(industry(), use_container_width=True)

    with tab7:
        st.caption('Data Professional Survey: Top 11 Programming Languages',)
        st.plotly_chart(programming(), use_container_width=True)
