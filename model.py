import pandas as pd

def preprocess_titanic(train_df, validate_df, test_df):
    encoded_df = []
    for df in [train_df, validate_df, test_df]:
        df.pclass = df.pclass.astype(int)
        df_encoded_columns = pd.get_dummies(df[['embark_town', 'sex']],
              drop_first=True).astype(int)
        encoded_df.append(pd.concat([df, df_encoded_columns],
                                    axis=1).drop(columns=['sex', 'embark_town']))
    return encoded_df

def preprocess_telco(train, validate, test):
    encoded_df = []
    
    for df in [train, validate, test]:
        yes_no_columns = ['multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']

        for col in yes_no_columns:
            df[col] = np.where(df[col] == 'Yes', 'Yes', 'No')
            
        encoded_columns = df.columns[df.nunique() < 10].tolist()
        
        df_encoded_columns = pd.get_dummies(df[encoded_columns], drop_first=True).astype(int)
        df = pd.concat([df, df_encoded_columns], axis=1).drop(columns=encoded_columns)
        encoded_df.append(df)
    
    return encoded_df