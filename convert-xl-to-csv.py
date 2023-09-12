import pandas as pd
import sys

#excel_file = pd.ExcelFile('./data_source/issues.xlsx')
excel_file = pd.ExcelFile(str(sys.argv[1]))
df = excel_file.parse(excel_file.sheet_names[0])
df.to_csv('outputs.csv', index=False)
