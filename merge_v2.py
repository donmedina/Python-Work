import pandas as pd
import os

path = "L:/resp/"
files = os.listdir(path)

xls = [f for f in files if f[-3] == 'xls']

df = pd.DataFrame()

for f in xls:
    data = pd.read_excel(path + f,'Planilha1')
    df = df.append(data)
    df.to_excel(path + "out.xls")
