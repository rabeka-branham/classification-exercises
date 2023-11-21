from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(dataframe):
    train, validate_test = train_test_split(dataframe, 
                                            train_size=.6, 
                                            random_state=913
                                           )
    validate, test = train_test_split(validate_test,
                                      test_size=0.50, 
                                      random_state=913
                                     )
    return train, validate, test

def prep_iris(dataframe):
    dataframe.columns = dataframe.columns.str.replace('.','_').str.lower()
    df = dataframe.drop(columns = ['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name':'species'})
    return df

def prep_titanic(dataframe):
    df = dataframe.drop(columns=['embarked','class','deck','age'])
    df.pclass = df.pclass.astype(object)
    df.embark_town = df.embark_town.fillna('Southampton')
    return df

def prep_telco(dataframe):
    df = dataframe.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'])
    df.internet_service_type = df.internet_service_type.fillna('No internet service')
    return df