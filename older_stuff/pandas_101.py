import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from tabulate import tabulate

pd.set_option('notebook_repr_html', True)

my_nums = pd.Series([12, 324, 56, 657, 567, 768, 78, 43, 213, 45, 56, 7, 87, 23, 32, 32])
print [[my_nums]]
xx = my_nums #.sort_values(inplace=True, ascending=False)
yy = [[xx]]
print type(yy)

# sys.exit()

input_file = r"t:\Users\yaniv\GoogleDrive\limor\DS\Part 2 - Tools\06 - The pandas module\pandas practice\San Francisco Crime\crimes.csv"

crimes = pd.read_csv(input_file, index_col="Dates", parse_dates=True, nrows=50)
# crimes = pd.read_csv(input_file, index_col="Dates")
# print crimes.head()
crimes_headers = crimes.columns
print tabulate(crimes, headers='keys', tablefmt='grid')


# print crimes.columns
# print crimes.info()

cat = crimes['Category'].drop_duplicates()
cat = crimes['Category']
print cat.unique()
print cat.nunique()
print cat.value_counts()
# print cat.str.len().plot()

xx = crimes['X']
xx.plot()
plt.show()

# print cat.head()
# print crimes.loc['2015-05-13 23:30:00']
# print crimes.iloc[xrange(3)]['Resolution']



