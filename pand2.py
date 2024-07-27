import pandas as pd
Ser1=pd.Series([23,2,42,95,45,45,19,28,34],index=['a','b','c','d','e','f','g','h','i'])
print("Top 3 biggest no.s")
#print(Ser1.sort_values().tail(3))
print(Ser1.sort_values(ascending = False).head(3))
print("3 smallest no.s are: \n")
#print(Ser1.sort_values().head(3))
print(Ser1.sort_values(ascending = False).tail(3))
