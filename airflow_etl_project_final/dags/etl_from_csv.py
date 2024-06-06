import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
import re

default_args= {
    'owner': 'Raymond',
    'start_date': datetime(2024, 6, 4)
}

with DAG(
    'etl_csv_files',
    description='from gdrive to postgres',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:
    files = {
        'user_behavior' : 'https://drive.google.com/file/d/1IQyPgSETeSMoN_bNbhkMKJP-5NWxqqhj/view?usp=sharing',
        'user_profile' : 'https://drive.google.com/file/d/1TQVPuMnTyuxmtZnSDckiZik3koEMqEtV/view?usp=sharing'
    }

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    def read_from_gdrive(url,file_name):
        url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
        df = pd.read_csv(url)
        print("Sample data :")
        print(df.head())
        df.to_csv(f'/opt/airflow/data/{file_name}.csv',index=False)

    @task()
    def get_files_user_behavior():
        file_name = list(files.keys())[0]
        url = files['user_behavior']
        df = read_from_gdrive(url,file_name)
        return df 

    @task()
    def get_files_user_profile():
        file_name = list(files.keys())[1]
        url = files['user_profile']
        df = read_from_gdrive(url,file_name)
        return df

    @task()
    def combine_files():
        # Read the dataframes
        df_user_behavior = pd.read_csv(f'/opt/airflow/data/{list(files.keys())[0]}.csv')
        df_user_profile = pd.read_csv(f'/opt/airflow/data/{list(files.keys())[1]}.csv')
 
        # Join df_user_behavior and df_user_profile on 'primary_key'
        df = df_user_behavior.set_index('primary_key').join(df_user_profile.set_index('primary_key'), how='inner', lsuffix='_cust', rsuffix='_purch').reset_index()

        print(df.head())

        df.to_csv(f'/opt/airflow/data/data_combine.csv', index=False)
    

    @task()
    def preprocess_data():
        df = pd.read_csv('/opt/airflow/data/data_combine.csv')
        
        # Handle missing values (example: fill missing numeric values with the mean)
        # df.fillna(df.mean(numeric_only=True), inplace=True)

        # Drop Col primary_key 
        df = df.drop(['primary_key'], axis = 1)

        #Function Edit column name to lower and _
        def camel_to_snake(name): 
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).replace('__', '_').lower() 

        # Apply the function to each column name
        df.columns = df.columns.map(camel_to_snake)

        # Remove duplicates if any
        df.drop_duplicates(inplace=True) 

        # Mengubah value fitur "Month" menjadi angka
        month_mapping = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'June':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        df['month'] = df['month'].map(month_mapping) 
        

        print("Preprocessed data is Success")
        print(df.head())
        df.to_csv('/opt/airflow/data/data_combine_preprocessed.csv', index=False)

    @task()
    def insert_to_db():
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_csv('/opt/airflow/data/data_combine_preprocessed.csv')

        df.to_sql('online_shoppers_intention', conn, index=False, if_exists='replace') 
        print("Success INSERT")

    start >> [get_files_user_behavior(), get_files_user_profile()] >> combine_files() >> preprocess_data() >> insert_to_db() >> end