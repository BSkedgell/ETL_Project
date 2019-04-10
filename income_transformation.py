#Import modules
import csv
import pandas as pd
from sqlalchemy import create_engine

def income_extract.py

#Select income for df to be transformed
income = income1[["Neighborhood", "Tract Number",]].copy()
income.head()

#Set index to "id"
income.index.names = ['id']
income.head()

#Reset index (now id column) to start at 1
income.index = income.index + 1
income.head()

#Rename columns to match what will be used in the Load process of the ETL
income = income.rename(columns={"Neighborhood":"name", "Tract Number":"tract_id"})
income.head()

#Run print if you want to see table in terminal
print(income.head())