import pandas as pd
import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt

title = st.title("Análisis de Vehiculos")
st.write('Raw Data')

data_view = pd.read_csv('vehicles_us.csv')

st.dataframe(data_view)

st.title('Histograma de anuncios de venta de coches')
hist_check = st.checkbox('Construir histograma')

if hist_check:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(data_view, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

days = data_view.groupby('days_listed')['model'].count()
st.header('Cantidad de Vehiculos / Días listados ')

st.bar_chart(days, x_label='Días listado', y_label='Cantidad de vehículos')


r2010 = data_view.query('model_year > 2014')[['type', 'price', 'model']]
mean_price = r2010.groupby('type')['price'].mean()

st.title('Precio Promedio por Vehículo en los últimos 5 años')
st.dataframe(mean_price)
st.bar_chart(mean_price, y_label='Precio en USD', x_label='Tipo de Vehículos')


cond_year = data_view.groupby('condition')['model'].count()
bar_button = st.button(
    'Da click para mostrar la condicion de los vehiculos', type='primary')
if bar_button:
    st.title('Vehicle condition')
    st.bar_chart(cond_year, horizontal=True, y_label='Condition',
                 x_label='Number of Vehicles')


p2010 = data_view[data_view.model_year >= 2000]

st.title('Disperción de los precios de los vehiculos con base en el kilometraje')
scat_check = st.checkbox('Mostrar Disperisón')

if scat_check:
    st.write()

    st.scatter_chart(p2010, x='odometer', y='price')
