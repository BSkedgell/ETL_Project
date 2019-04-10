import csv
import pandas as pd

def transform_data(income):
    
#Select income1 for df to be transformed and drop rows that have incomplete columns
    income1 = income.dropna(how="any")

#Rename the columns
    income1 = income1.rename(columns=
                         {"Year": "year", "Amount": "amount", "Tract Number": "tract_id", "Neighborhood": "neighborhood"})

    income2 = income1[["year", "amount", "tract_id", "neighborhood"]].copy()

    #Set index to "id"
    income2['id'] = income2.index + 1

    #Rename columns in median_income table to match what will be used in the Load process of the ETL
    median_income = income2[["id", "amount", "year", "tract_id"]].copy()

    #Rename columns in neighborhoods table to match what will be used in the Load process of the ETL
    neighborhoods = income2[["id", "neighborhood", "tract_id"]].copy()

    return (median_income, neighborhoods)