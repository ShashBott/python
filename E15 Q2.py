import pandas as pd
df = pd.read_excel(r'E:\python files\Book1.xlsx')
df.to_csv(r'E:\python files\Book1.csv', index = False)
print(df)
