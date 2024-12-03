import pandas as pd
import plotly.express as px

df = pd.read_csv('data/all_image_gps.csv')

fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name="image_name", hover_data=["category"], zoom=18)
fig.update_layout(map_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()