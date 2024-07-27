import pandas as pd
sent=input("Enter a sentence")
d={}
sent=sent.upper()
for ch in sent:
    if ch in "AEIOU":
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
s1=pd.Series(d)
print(s1)
