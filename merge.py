import pandas as pd

Path = "L:/resp/"
arq_excel = [Path + "PRRJ06170001.xlsx",Path + "PRRJ06170002.xlsx"] #This code works only with XLSX files

excel = [pd.ExcelFile(name) for name in arq_excel]

sheets = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excel]

sheets[1:] = [df[1:] for df in sheets[1:]]

combined_excel = pd.concat(sheets)

combined_excel.to_excel(Path + "Comb.xlsx", header=False, index=False)