import pandas as pd

file = pd.read_csv("machine-readable.csv",header=0,index_col="Period",names=['col1','col2','col3','cl4','cl5','c3','c7'])
print(file.tail())
     