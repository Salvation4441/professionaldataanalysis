import os
import pandas as pd
import plotly.express as px
import streamlit as st
import pandasql as ps
import plotly.graph_objects as go

pd.options.display.float_format = '{:,.2f}'.format

# get the path the .csv file

path = os.path.join('classes', 'Survey.csv')

# read
data = pd.read_csv(path, encoding='latin1')


@st.cache
def country_salary():
    df = ps.sqldf(
        "SELECT Country, AVG(Salary) AS Average_Salary FROM data GROUP BY Country ORDER BY Average_Salary DESC")

    # df = data.pivot_table(index=['Resident Country'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', ascending=False, inplace=True)
    # title = 'Top 10 Data Professional Survey Average Salary',
    # fig = px.scatter_geo(df,
    #                      locations=df['Resident Country'],
    #                      locationmode='country names',
    #                      color=df['Resident Country'],
    #                      text=df['Average_Salary'],
    #                      hover_name=df['Resident Country'],
    #                      height=600
    #                      )
    # fig.update_geos(projection_type="orthographic", showcountries=True, )
    # fig.update_layout(height=700, margin={"r": 0, "t": 0, "l": 0, "b": 0}, )
    # return fig

    # country_map = dict(type='choropleth',
    #                    locations=df['Country'],
    #                    locationmode='country names',
    #                    z=df['Average_Salary'],
    #                    # reversescale=True,
    #                    text=df['Country'],
    #
    #                    colorscale='earth',
    #                    colorbar={'title': 'Number of Respondents'},
    # )
    # # title = 'Top 10 Data Professional Survey Average Salary',
    # layout = dict(geo=dict(showframe=False, projection={'type': 'mercator'}))
    # fig = go.Figure(data=[country_map], layout=layout)
    #
    # fig.update_layout(height=700,width=900, margin={"r": 0, "t": 0, "l": 0, "b": 0}, )
    #
    fig = px.scatter_geo(df,
                         locations=df['Country'],
                         locationmode='country names',
                         color=df['Country'],
                         # text=df['Country'],
                         labels={'Average_Salary': 'Average Salary(K)'},
                         hover_name=df['Country'],


                         )
    fig.update_geos(projection_type="orthographic", visible=True, showcountries=True, )
    fig.update_layout(height=700, width=900, margin={"r": 0, "t": 0, "l": 0, "b": 0}, )
    fig.update_layout(showlegend=False)

    result = [tuple(df.iloc[i]) for i in range(5)]
    return fig, result


def ten_country():
    # df = data.pivot_table(index=['Resident Country'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', ascending=False, inplace=True)

    df = ps.sqldf(
        f"SELECT Country, AVG(Salary) AS Average_Salary FROM data GROUP BY Country ORDER BY Average_Salary DESC")

    fig = px.bar(df.head(10),
                 y='Resident Country',
                 x='Average_Salary',
                 color='Resident Country',
                 labels={'Resident Country': 'Country', 'Average_Salary': 'Average Salary(K)'},
                 orientation='h'
                 )
    fig.update_layout(showlegend=False)
    return fig


def gender():
    # df = data.pivot_table(index=['Gender'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', ascending=False, inplace=True)
    df = ps.sqldf(f"SELECT Gender,Salary, AVG(Salary) AS Average_Salary \
    FROM data GROUP BY Gender ORDER BY Average_Salary DESC")

    fig = px.bar(df,
                 x='Gender',
                 y=['Salary', 'Average_Salary'],
                 color='Salary',
                 title='Gender with their Salary',
                 labels={'Salary': 'Salary(K)', 'value': 'Average Salary(K)'},
                 height=600
                 )
    #  values='pop', names='country'
    fig.update_layout(showlegend=False)
    #  values='pop', names='country'
    fig.update_layout(showlegend=False)
    return fig


def age_group():
    # df = data.pivot_table(index=['Age_group'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)

    df = ps.sqldf(f"SELECT Age_group, AVG(Salary) AS Average_Salary \
    FROM data GROUP BY Age_group ORDER BY Average_Salary DESC")

    fig = px.bar(df,
                 x='Age_group',
                 y=['Average_Salary'],
                 color='Age_group',
                 labels={'Age_group': 'Age Group', 'value': 'Average Salary(K)'},
                 title='Average Salary with its Age Group',
                 height=600)
    fig.update_layout(showlegend=False)
    return fig


def edu():
    # df = data.pivot_table(index=['Education'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', ascending=False, inplace=True)

    df = ps.sqldf(f"SELECT Education, AVG(Salary) AS Average_Salary \
    FROM data GROUP BY Education ORDER BY Average_Salary DESC")

    fig = px.bar(df,
                 y='Education',
                 x='Average_Salary',
                 color='Education',
                 title='Education level with their Salary',
                 labels={'Average_Salary': 'Average Salary(K)'},
                 orientation='h',
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


#  Ethnicity
def ethnicity():
    # df = data.groupby('Ethnicity').filter(lambda x: x['Ethnicity'].count() >= 2)
    #
    # df = df.pivot_table(index=['Ethnicity'], values='Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Salary', ascending=False, inplace=True)

    param = 2
    df = ps.sqldf(f"SELECT Ethnicity, AVG(Salary) AS Average_Salary \
    FROM data GROUP BY Ethnicity HAVING Count (Ethnicity)> {param} \
    ORDER BY Average_Salary DESC")

    fig = px.bar(df,
                 y='Ethnicity',
                 x='Average_Salary',
                 color='Ethnicity',
                 title='Ethnicity with their Salary',
                 labels={'Average_Salary': 'Average_Salary(K)'},
                 height=600
                 )
    #  values='pop', names='country'
    fig.update_layout(showlegend=False)
    return fig


# role
def role():
    # df = data.groupby('Which Title Best Fits your Current Role?'). \
    #     filter(lambda x: x['Which Title Best Fits your Current Role?'].count() >= 2)
    # df = df.pivot_table(index=['Which Title Best Fits your Current Role?'], values='Average_Salary', aggfunc='mean')
    #
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', inplace=True)
    # df.columns = ['Role', 'Count']

    param = 2
    df = ps.sqldf(f"SELECT Current_Role,Salary,Count(Current_Role) AS Number \
    FROM data GROUP BY Current_Role HAVING Count (Current_Role)> {param} \
    ORDER BY Number DESC")

    fig = px.bar(df,
                 y='Current_Role',
                 x=['Salary', 'Number'],
                 color='Salary',
                 title='Job roles with number of respondents present for that job',
                 labels={'Current_Role': 'Role', 'value': 'Number of workers'},
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


# industry
def industry():
    # df = data.groupby('What Industry do you work in?'). \
    #     filter(lambda x: x['What Industry do you work in?'].count() >= 10)
    #
    # df = df.pivot_table(index=['What Industry do you work in?'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', inplace=True)
    # df.columns = ['Industry', 'Salary']

    param = 10
    df = ps.sqldf(f"SELECT Industry,Salary, AVG(Salary) AS Average_Salary \
    FROM data GROUP BY Industry HAVING Count (Industry)> {param} \
    ORDER BY Average_Salary DESC")

    fig = px.bar(df,
                 y='Industry',
                 x=['Salary', 'Average_Salary'],
                 color='Salary',
                 title='Base salary for programming languages',
                 labels={'value': 'Average Salary(K)'},
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


# programming
def programming():
    # df = data.groupby('Favorite Programming Language'). \
    #     filter(lambda x: x['Favorite Programming Language'].count() >= 2)
    #
    # df = df.pivot_table(index=['Favorite Programming Language'], values='Average_Salary', aggfunc='mean')
    # df.reset_index(inplace=True)
    # df.sort_values(by='Average_Salary', ascending=False, inplace=True)
    # df.columns = ['Programming Language', 'Salary']

    param = 2
    df = ps.sqldf(f"SELECT Programming_Language,Salary,Count(Programming_Language) AS Number \
    FROM data GROUP BY Programming_Language HAVING Count (Programming_Language)> {param} \
    ORDER BY Number DESC")
    rows, cols = df.shape
    fig = px.bar(df,
                 y='Programming_Language',
                 x=['Salary', 'Number'],
                 color='Salary',
                 labels={'value': 'Number of Respondents', 'Programming_Language': 'Programming Language'},
                 title=f'Data Professional Survey: Top {rows} Programming Languages',
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


# HAPPY INDEX

def salary():
    df = data.groupby('Happiness_Index(Salary)'). \
        filter(lambda x: x['Happiness_Index(Salary)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Salary)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 x='Happiness_Index(Salary)',
                 y='Salary',
                 color='Salary',
                 labels={'Happiness_Index(Salary)': 'Status', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


def work():
    df = data.groupby('Happiness_Index(Work/Life Balance)'). \
        filter(lambda x: x['Happiness_Index(Work/Life Balance)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Work/Life Balance)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 x='Happiness_Index(Work/Life Balance)',
                 y='Salary',
                 color='Salary',
                 labels={'Happiness_Index(Work/Life Balance)': 'Satisfactory', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


def coworker():
    df = data.groupby('Happiness_Index(Coworkers)'). \
        filter(lambda x: x['Happiness_Index(Coworkers)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Coworkers)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 x='Happiness_Index(Coworkers)',
                 y='Salary',
                 color='Salary',
                 labels={'Happiness_Index(Coworkers)': 'Satisfactory', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


def management():
    df = data.groupby('Happiness_Index(Management)'). \
        filter(lambda x: x['Happiness_Index(Management)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Management)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 y='Happiness_Index(Management)',
                 x='Salary',
                 color='Happiness_Index(Management)',
                 labels={'Happiness_Index(Management)': 'Satisfactory', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


def upward():
    df = data.groupby('Happiness_Index(Upward Mobility)'). \
        filter(lambda x: x['Happiness_Index(Upward Mobility)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Upward Mobility)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 y='Happiness_Index(Upward Mobility)',
                 x='Salary',
                 color='Salary',
                 labels={'Happiness_Index(Upward Mobility)': 'Satisfactory', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig


def new_things():
    df = data.groupby('Happiness_Index(Learning New Things)'). \
        filter(lambda x: x['Happiness_Index(Learning New Things)'].count() > 2)
    df = df.pivot_table(index=['Happiness_Index(Learning New Things)'], values='Salary', aggfunc='mean')
    df.reset_index(inplace=True)
    df.sort_values(by='Salary', ascending=False, inplace=True)

    fig = px.bar(df,
                 x='Happiness_Index(Learning New Things)',
                 y='Salary',
                 color='Salary',
                 labels={'Happiness_Index(Learning New Things)': 'Satisfactory', },
                 height=600
                 )
    fig.update_layout(showlegend=False)
    return fig
