from sklearn.model_selection import train_test_split

def prep_iris(dataframe):
    '''
    This function takes in a dataframe & drops the 'species_id' & 'measurement_id' columns as well as renames the 'species_name' column to 'species'. It then returns the prepped dataframe.
    '''
    df = dataframe.drop(columns = ['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name':'species'})
    return df

def prep_titanic(dataframe):
    '''
    This function takes in a dataframe & drops the 'embarked', 'class' ,'deck', & 'age' columns, casts the 'pclass' column as a string/an object to make it categorical, & fills the 2 null values in the 'embark_town' column with the most frequent value 'Southampton'. It then returns the prepped dataframe.
    '''
    df = dataframe.drop(columns=['embarked','class','deck','age'])
    df.pclass = df.pclass.astype(object)
    df.embark_town = df.embark_town.fillna('Southampton')
    return df

def prep_telco(dataframe):
    '''
    This function takes in a dataframe & drops the 'payment_type_id', 'internet_service_type_id', & 'contract_type_id' columns, fills the null values in the 'internet_service_type' column with 'No internet service', & replaces the empty values in the 'total_charges' column with '0.0' & casts the column as a float. It then returns the prepped dataframe.
    '''
    df = dataframe.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'])
    df.internet_service_type = df.internet_service_type.fillna('No internet service')
    df.total_charges = df.total_charges.replace(' ','0.0').astype('float')
    return df

def split_data(dataframe, col):
    '''
    This function takes in a dataframe & the column on which you want to stratify. It first splits the dataframe by 60/40 & sets them as new dataframes to the variables: train & validate_test. It then splits the validate_test dataframe 50/50 & sets them as new dataframes to the variables: validate & test. It them returns the variables: train, validate, & test.
    '''
    train, validate_test = train_test_split(dataframe, 
                                            train_size=.6, 
                                            random_state=913,
                                            stratify=dataframe[col]
                                           )
    validate, test = train_test_split(validate_test,
                                      test_size=0.50, 
                                      random_state=913,
                                      stratify=validate_test[col]
                                     )
    return train, validate, test