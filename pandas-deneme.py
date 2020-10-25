import pandas as pd

df = pd.read_csv("appstore_games.csv")
df.drop(columns = ["Subtitle","URL","Icon URL","In-app Purchases"],inplace = True)
df.dropna()
result = df
result = df[df["Average User Rating"] >=4.5].sort_values("User Rating Count",ascending = False)[["Name","Average User Rating"]]
result = df["Size"].sum()/1024/1024/1024/1024



print(result)