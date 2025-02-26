import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title('Analysis of World Covid-19 Vaccination Progress')
st.text("")
st.text("")
st.image("d41586-019-03635-9_17408652.gif")
st.markdown("---")
sidebar = st.sidebar
sidebar.title('Analysis of World Covid-19 Vaccination Progress')


def viewDataset():
    st.header('Data Used in Project')
    datasets = ['Country Data', 'Manufacturer Data']
    selData = st.selectbox(options=datasets, label='Select Dataset to View')
    if selData == datasets[0]:
        dataframe = analysis_cnt.getDataframe()
        showDetails(dataframe)
    elif selData == datasets[1]:
        dataframe = analysis_mnf.getDataframe()
        showDetails(dataframe)


def showDetails(dataframe):
    with st.spinner("Loading Data..."):
        st.dataframe(dataframe[:5000])

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analyseManufacturers():

    st.header('Vaccine Manufacturers Total Count')

    data = analysis_mnf.getMnfCount()
    st.plotly_chart(plotBar(data, "Pfizer is the most popular Vaccine Manufacturer",
                            "No. of Vaccinations", "Manufacturer"), use_container_width=True)

    st.header('Increase in Vaccine Manufacturing over time')
    st.image('plotImages/man_line.png', use_column_width=True)


def countrywiseAnalysis():

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations',
                             'Country Name', 'No. of Vaccinations'))

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries',
                                   'Country Name', 'No. of Vaccinations'))
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries',
                                   'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'))
    st.markdown("---")

    st.header('Daily Vaccinations in Countries')
    st.image('plotImages/daily_vacc_line.png', use_column_width=True)

    st.header('Fully Vaccinated Peoples in Countries')
    st.image('plotImages/fully_vacc_line.png', use_column_width=True)

    st.header('No. of Vaccinated People in Countries')
    st.image('plotImages/people_vacc_line.png', use_column_width=True)

    st.header('Total Vaccinations done in Countries')
    st.image('plotImages/total_vacc_line.png', use_column_width=True)

    st.header('Vaccination done per 100 in Countries')
    st.image('plotImages/total_per100_line.png', use_column_width=True)


def vaccineAnalysis():
    st.header('Country Vaccinations with respect to vaccine Manufacturer')
    selVaccine = st.selectbox(
        options=analysis_cnt.getVaccines(), label="Choose vaccine to continue")

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations',
                             'Country Name', 'No. of Vaccinations'))

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries',
                                   'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

   


sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyse Manufacturers',
           'Analyse Country', 'Analyse Country By Vaccine',]
choice = sidebar.selectbox(options=options, label="Choose Action")

with st.spinner("Please Wait for Some Time..."):
    analysis_mnf = Analyse(r"datasets/manufacturer.csv")
    analysis_cnt = Analyse(r"datasets/country.csv")

    if choice == options[0]:
        viewDataset()
    elif choice == options[1]:
        analyseManufacturers()
    elif choice == options[2]:
        countrywiseAnalysis()
    elif choice == options[3]:
        vaccineAnalysis()














 









    


                                    

