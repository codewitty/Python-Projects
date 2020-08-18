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


nom = ArcGIS()
n = nom.geocode("3995 23rd Street, San Francisco, CA 94114")
print (n.latitude, n.longitude)

# Use DataFrame to pass addresses to geoLocator

df1["Address"] = df1["Address"] + " , " + df1["City"] + " , " + df1["State"] + " , " + df1["Country"]

print(df1)

# Gecode each row

df1["Co-ordinates"] = df1["Address"].apply(nom.geocode)
