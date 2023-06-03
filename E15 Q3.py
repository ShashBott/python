import pandas as pd
df = pd.read_excel(r'E:\python files\Book1.xlsx')

df.columns =['ticker', 'eps', 'revenue', 'price','people']
  

print(df)
