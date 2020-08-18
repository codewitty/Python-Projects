import pandas
from geopy.geocoders import ArcGIS

df1 = pandas.read_csv("supermarkets.csv")
df2 = pandas.read_json("supermarkets.json")
df3 = pandas.read_excel("supermarkets.xlsx")
df4 = pandas.read_csv("supermarkets-commas.txt")
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep = ";")
df6 = df5.set_index("ID")

print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print(type(df6))
# Check rows and colums
print(df6.shape)
print(df6.shape[0])
print(df6.shape[1])
