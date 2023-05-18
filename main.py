import pandas as pd
import plotly.express as px

df = pd.read_csv("star_with_gravity.csv")
df.head()

df.drop(['Unnamed: 0'],axis =1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

fig = px.bar(x=name, y=mass)
fig.show()


fig = px.bar(x=name, y=radius)
fig.show()


fig = px.bar(x=name, y=dist)
fig.show()


fig = px.bar(x=name, y=gravity)
fig.show()


