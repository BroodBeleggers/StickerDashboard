import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Read data from CSV file in GitHub
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRUYAKrovEdIaaIi9UPDN5tjRHIxFZ6Lriwe9f5qd9SMbJx2B3DE4WV-GHHRS7p7Mf4RxgPB-EtZ9IR/pubhtml'
df = pd.read_csv(url, sep=';')

# Create map figure
fig = go.Figure(data=go.Scattermapbox(
    lat=df['Latitude'],
    lon=df['Longitude'],
    mode='markers',
    marker=go.scattermapbox.Marker(size=14),
    text=df['Location'],
))

fig.update_layout(
    mapbox_style="open-street-map",
    geo_scope='world',
    autosize=True,
    mapbox=dict(
        center=dict(
            lat=df['Latitude'].mean(),
            lon=df['Longitude'].mean(),
        ),
        zoom=1,
    ),
)

# Streamlit code
st.plotly_chart(fig)

selected_location = st.selectbox('Kies een locatie', df['Location'])

if st.button('Toon afbeelding'):
    selected_image = df[df['Location'] == selected_location]['ImageURL'].values[0]
    st.image(selected_image)
