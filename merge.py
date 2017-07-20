import pandas as pd

arq_excel = ["PRRJ06170001.xls",
"PRRJ06170002.xls",
"PRRJ06170003.xls",
"PRRJ06170058.xls",
"PRRJ06170059.xls",
"PRRJ06170060.xls",
"PRRJ06170061.xls",
"PRRJ06170062.xls",
"PRRJ06170063.xls",
"PRRJ06170064.xls",
"PRRJ06170065.xls",
"PRRJ06170066.xls",
"PRRJ06170075.xls",
"PRRJ06170076.xls",
"PRRJ06170077.xls",
"PRRJ06170078.xls",
"PRRJ06170079.xls",
"PRRJ06170080.xls"
]

excel = [pd.ExcelFile(name) for name in arq_excel]

sheets = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excel]

sheets[1:] = [df[1:] for df in sheets[1:]]

combined_excel = pd.concat(sheets)

combined_excel.to_excel("Comb.xlsx", header=False, index=False)