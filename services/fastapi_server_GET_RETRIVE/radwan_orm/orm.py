"""
    ORM main module for integrate the db
"""

from .Databases import sqlite3 as sqlite_tools
from .Databases import mysql as mysql_tools
from .Databases import base as Fields

# import Databases.sqlite3 as sqlite_tools
# import Databases.mysql as mysql_tools
# from Databases.base import Fields

class RadwanORM :

    def __init__(self) -> None:

        self.__dbs = {
            'mysql' : mysql_tools.MySql,
            'sqlite3' : sqlite_tools.Sqlite3,
        }

    def __get_db_model (self, dbtype,config) : 
        if dbtype == 'sqlite3' : 
            cls = sqlite_tools.Sqlite3(config) 
        elif dbtype == 'mysql' : 
            cls = mysql_tools.MySql(config) 
        return cls
    
    def connect(self, dbtype,config:dict) : 
        if not self.is_supported_db(dbtype) :
            raise ValueError(f'"{dbtype}" not supproted at this orm, system only supprted : {self.get_all_db}')
        if len(config) == 0 : 
            raise ValueError('Config cannot be empty !')
        
        return self.__get_db_model(dbtype,config)

    @property
    def __retrive_dbvals (self) : 
        return [key for key,val in self.__dbs.items()]
    
    @property    
    def get_all_db(self) : 
        return self.__retrive_dbvals
    
    def is_supported_db(self,dbtype):
        return dbtype in self.__retrive_dbvals


 