import mysql.connector
from inspect import getmembers
from .base import Schema

class MySql:
    def __init__(self,config:dict) -> None:
        if 'NAME' not in config or 'HOST' not in config or 'PASSWORD' not in config or 'USER' not in config :
            raise ValueError("There is missing attrs, the accepted attrs : USER, PASSWORD, HOST, NAME.")
        
        name = config['NAME']
        host = config['HOST']
        password = config['PASSWORD']
        user = config['USER']

        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )

        self.cur = self.db.cursor()

        self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
        self.cur.execute(f"USE {name};")
    
    def manage (self, model):
        """
          control the database table
        """
        schema = Schema(db=self.db,cur=self.cur,model=model)
        schema.db_type = 'mysql'
        return schema
        # return Schema(cur=self.cur,model=model)
    
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

        model_id = f'{self.table_name}_id INTEGER PRIMARY KEY AUTO_INCREMENT,'
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
        self.cur.execute(query)
        self.db.commit()
    
    def delete_table(self,model:object) : 
        """
            Delete Table From db
        """
        self.table_name = model.__name__
        query = f"drop table if exists {self.table_name};"
        self.cur.execute(query)
        self.db.commit()


