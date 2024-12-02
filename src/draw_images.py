import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
df = pd.read_csv('data/all_image_gps.csv')
import plotly.express as px

fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name="image_name", zoom=3, height=300)
fig.update_layout(map_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()