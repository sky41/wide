import pandas as pd

# read an excel file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_excel("附件_二季度.xlsx"))

# show the dataframe
print(df)
