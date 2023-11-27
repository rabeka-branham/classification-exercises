import os
from env import get_db_url
import pandas as pd

def check_file_exists(filename, query, url):
    '''
    This function checks if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not exist, it will create the file & return it to us as a dataframe.
    '''
    if os.path.exists(filename):
        print('File exists - reading CSV file')
        df = pd.read_csv(filename)
    else:
        print('File does not exist - creating CSV file')
        df = pd.read_sql(query,url)
        df.to_csv(filename)
    return df

def get_titanic_data():
    '''
    This function sets the filename to 'titanic.csv', the url to read from the codeup mysql db 'titanic_db', & the query.

    It will then run the function check_file_exists() using these parameters. This function checks if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not exist, it will create the file & return it to us as a dataframe.
    '''
    filename = 'titanic.csv'
    url = get_db_url('titanic_db')
    query = 'select * from passengers'

    df = check_file_exists(filename,query,url)
    
    return df

def get_iris_data(): 
    '''
    This function sets the filename to 'iris.csv', the url to read from the codeup mysql db 'iris_db', & the query.

    It will then run the function check_file_exists() using these parameters. This function checks if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not exist, it will create the file & return it to us as a dataframe.
    '''
    filename = 'iris.csv'
    url = get_db_url('iris_db')
    query = '''
            select * from measurements
            join species using (species_id)
            '''
    
    df = check_file_exists(filename,query,url)
    
    return df
    
def get_telco_data():
    '''
    This function sets the filename to 'telco.csv', the url to read from the codeup mysql db 'telco_churn', & the query.

    It will then run the function check_file_exists() using these parameters. This function checks if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not exist, it will create the file & return it to us as a dataframe.
    '''
    filename = 'telco.csv'
    url = get_db_url('telco_churn')
    query = '''
        select * from customers
        join contract_types using (contract_type_id)
        join internet_service_types using (internet_service_type_id)
        join payment_types using (payment_type_id);
        '''
    
    df = check_file_exists(filename,query,url)
    
    return df