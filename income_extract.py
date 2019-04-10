
#Import modules
import csv
import pandas as pd
from sqlalchemy import create_engine

#Store CSV into DataFrame
income1 = pd.read_csv('https://usc.data.socrata.com/api/views/kygc-fzgm/rows.csv?accessType=DOWNLOAD')
income1.head()

#Run print if you want to see table in terminal
print(income1.head())
