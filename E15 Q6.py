import pandas as pd
import numpy as np

a=pd.read_excel(r'E:\python files\Book1.xlsx')
print(a)
print("\n")

b=a.to_csv(r'E:\python files\Book1.csv',index=False)
c=pd.read_csv(r'E:\python files\Book1.csv')
print(c)
print("\n")

a.columns=['ticker','eps','revenue','price','people']
print(a)
print("\n")

a=a.replace("n.a.",np.nan)
a=a.replace("not available",np.nan)
a['revenue']=a['revenue'].apply(lambda x:x if x>0 else np.nan)
print(a)
print("\n")

a=a.fillna(0)
print(a)
print("\n")

a['people']=a['people'].replace([0],'sam walton')
print(a)
