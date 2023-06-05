import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Read data from Google Sheets
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSiZdikc0W4OuCxPikz27_QtIek9hD1DPIPi43SxHdiNaXUiNpmuD0DV9hC25RV6J4sFDb1LpzaUtb6/pub?output=csv'
df = pd.read_csv(url, sep=',')

# Sort data alphabetically by location
df = df.sort_values('Location')

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
    height=600,
    mapbox=dict(
        center=dict(
            lat=df['Latitude'].mean(),
            lon=df['Longitude'].mean(),
        ),
        zoom=1,
    ),
)

# Streamlit code
# Set wide layout
st.set_page_config(layout="wide", page_title="B.R.O.O.D. is overal")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# Create a layout with two columns
col1, col2 = st.columns([5,2])

# Show map in the left column
col1.plotly_chart(fig, use_container_width=True)

## Function to extract file_id and create new URL
#def create_direct_link(url):
#    # Extract the file_id from the URL
#    file_id = url.split('=')[2]
#    # Create a new URL that directly accesses the file
#    return f'https://drive.google.com/uc?export=view&id={file_id}'

## Apply function to ImageURL column
#df['ImageURL'] = df['ImageURL'].apply(create_direct_link)

# Create selection box and button in the right column
selected_location = col2.selectbox('Selecteer een locatie', df['Location'])
if col2.button('Toon afbeelding'):
    selected_image = df[df['Location'] == selected_location]['ImageURL'].values[0]
    col2.image(selected_image, width=300) # Control the width of the image
