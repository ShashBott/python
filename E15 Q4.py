import numpy as np
import pandas as pd
df = pd.read_excel(r'E:\python files\Book1.xlsx')
na_values = ['n.a.','not available','""','-1'] # add all values that should be converted to np.nan
df=pd.read_excel('Book1.xlsx',na_values= na_values, keep_default_na = False)
print(df)
