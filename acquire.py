import os
from env import get_db_url
import pandas as pd


def get_titanic_data():
    filename = 'titanic.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        url = get_db_url('titanic_db')
        query = 'select * from passengers'
        df = pd.read_sql(query,url)
        df.to_csv(filename)
        return df

def get_iris_data(): 
    filename = 'iris.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        url = get_db_url('iris_db')
        query = 'select * from species'
        df = pd.read_sql(query,url)
        df.to_csv(filename)
        return df
    
def get_telco_data():
    filename = 'telco.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        url = get_db_url('telco_churn')
        query = '''
            select * from customers
            join contract_types using (contract_type_id)
            join internet_service_types using (internet_service_type_id)
            join payment_types using (payment_type_id);
            '''
        df = pd.read_sql(query,url)
        df.to_csv(filename)
        return df






