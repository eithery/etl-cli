import os
from dotenv import load_dotenv
from typing import Dict

_DEFAULT_DB_DIALECT = 'mssql'
_DEFAULT_ODBC_DRIVER = 'ODBC Driver 17 for SQL Server'
_DEFAULT_DB_HOST = 'localhost'
_DEFAULT_DB_INSTANCE_NAME = ''
_DEFAULT_DB_NAME = 'etl_db'
_DB_USER_VAR_NAME = 'ETL_DB_USER'
_DB_PASSWORD_VAR_NAME = 'ETL_DB_PASSWORD'


class Database:
    def __init__(self, settings: Dict[str, str]):
        load_dotenv()
        dialect = settings.get('dialect', _DEFAULT_DB_DIALECT)
        driver = settings.get('driver', _DEFAULT_ODBC_DRIVER)
        host = settings.get('host', _DEFAULT_DB_HOST)
        instance_name = settings.get('instance_name', _DEFAULT_DB_INSTANCE_NAME)
        db_name = settings.get('db_name', _DEFAULT_DB_NAME)
        user_name = os.getenv(_DB_USER_VAR_NAME)
        pwd = os.getenv(_DB_PASSWORD_VAR_NAME)
        connection_type = settings.get('connection', 'default')
        prefix = '' if connection_type.lower() == 'sspi' else f'{user_name}:{pwd}@'
        self._connection_string = f'mssql+pyodbc://{prefix}{host}/{db_name}?driver={driver}'


    @property
    def dialect(self):
        return _DB_DIALECT


    @property
    def driver(self):
        return _ODBC_DRIVER


    @property
    def host(self):
        return self._host or _DEFAULT_DB_HOST


    @property
    def instance_name(self):
        return _DB_INSTANCE_NAME


    @property
    def db_name(self):
        return _DB_NAME


    @property
    def user_name(self):
        return self._user_name


    @property
    def db_password(self):
        return self._password


    @property
    def connection_string(self):
        return f'mssql+pyodbc://{prefix}{self.host}/{self.db_name}?driver={self.driver}'
