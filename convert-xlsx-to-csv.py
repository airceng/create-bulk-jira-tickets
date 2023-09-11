import pandas as pd
import sys

df = pd.read_excel(str(sys.argv[1]),sheet_name=str(sys.argv[2]), header=0)
df.to_csv(str(sys.argv[3]), index=False)
