import sqlite3
from inspect import getmembers
from .base import Schema

class Sqlite3():
    
    
    def __init__(self, config:dict) -> None:

        if not 'NAME' in config :
            raise ValueError("NAME field not founded in the config of sqlite3 db ")
        dbname = config['NAME'] if '.sqlite3' or '.db' in config['NAME'] else str(config['NAME']) + '.sqlite3'

        self.db = sqlite3.connect(dbname)

        self.db.execute("PRAGMA foreign_keys=1;")
        self.db.commit()
        

    
    def manage (self, model):
        """
          control the database table
        """
        schema = Schema(db=self.db,model=model)
        schema.db_type = 'sqlite3'
        return schema

    def create_table (self, model:object) : 
        """
            Create Table with given
            model name, and fields 
            which wil be the class attributes
        """
        self.table_name = model.__name__
        self.fields = []

        append = False
        for i in getmembers(model) :
            key,val = i[0], i[1]
            if append:
                self.fields.append({
                    key:val
                })
            if key == '__weakref__':
                append = True

        str_fields = ""
        has_next = True
        index = 0

        model_id = f'{self.table_name}_id INTEGER PRIMARY KEY AUTOINCREMENT,'
        str_fields += model_id
        for field in self.fields :

            try : 
                self.fields[index + 1]
            except IndexError : 
                has_next = False

            for key,val in field.items() :
                if "FOREIGN" not in val :
                    str_fields += f"{key} {val}" 
                else:
                    str_fields += str(val).replace('@KEY@',f'{self.table_name}_id')
            if has_next :
                str_fields += ','

            index += 1
            
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({str_fields});"
        self.db.execute(query)
        self.db.commit()
    
    def delete_table(self,model:object) : 
        """
            Delete Table From db
        """
        self.table_name = model.__name__
        query = f"drop table if exists {self.table_name};"
        self.db.execute(query)
        self.db.commit()

