import streamlit as st
import pandas as pd
import os
import time

from classes.helper import gender, age_group, edu, ethnicity, role, industry, programming, salary, work, coworker, \
    management, new_things, upward

st.set_page_config(page_title='Survey', layout='wide', initial_sidebar_state='expanded', )

# link css
css_path = os.path.join('static', 'style.css')
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title('😍:blue[Happy Index]')

# add_selectbox = st.selectbox(
#     "How would you like to be contacted?",
#     ("Happiness_Index(Salary)", "Home phone", "Mobile phone")
# )
with st.expander("Happiness Index", expanded=True):
    tabs = ['Salary', 'Work/Life Balance', 'Coworkers', 'Management', 'Upward Mobility', 'Learning New Things']
    #
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tabs)
    with tab1:
        st.caption('How Happy are you in your Current Position with the following? (Salary)')
        st.plotly_chart(salary(), use_container_width=True)
    #
    with tab2:
        st.caption('How Happy are you in your Current Position with the following? (Work/Life Balance)', )
        st.plotly_chart(work(), use_container_width=True)

    with tab3:
        st.caption('How Happy are you in your Current Position with the following? (Coworkers)')
        st.plotly_chart(coworker(), use_container_width=True)

    with tab4:
        st.caption('How Happy are you in your Current Position with the following? (Management)')
        st.plotly_chart(management(), use_container_width=True)

    with tab5:
        st.caption('How Happy are you in your Current Position with the following? (Upward Mobility)')
        st.plotly_chart(upward(), use_container_width=True)

    with tab6:
        st.caption('How Happy are you in your Current Position with the following? (Learning New Things)')
        st.plotly_chart(new_things(), use_container_width=True)
