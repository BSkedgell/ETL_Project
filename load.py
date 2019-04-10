from sqlalchemy import create_engine

connection_string = "root:root@localhost/income"
engine = create_engine(f'mysql+pymysql://{connection_string}')

def loaded_data(income):

    income[0].to_sql(name='median_income', con=engine, if_exists='append', index=False)

    #Use pandas to load csv converted DataFrame into database
    income[1].to_sql(name='neighborhoods', con=engine, if_exists='append', index=False)

    return "completed!"