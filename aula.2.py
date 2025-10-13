import pandas as pd
import streamlit as st
import plotly.express as st

dataset = pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')

fig = px.choropleth(dataset,
                    locations=dataset['iso3'],
                    color=dataset['latitude'],
                    hover_name=dataset['nome'])
fig.update_layout(title='Mapa Coroplético dos Países',
                  geo_scope='world')
st.plotly_chart(fig,
                use_container_widht=True,
                theme='streamlit')
