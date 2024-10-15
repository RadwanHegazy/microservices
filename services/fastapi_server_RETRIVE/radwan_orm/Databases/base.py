"""
 db Controller
"""
from inspect import getmembers
from datetime import datetime

class Schema :
    db_type = ""
    """
        For writing the SQL code
    """
    def __init__(self, model, db,cur=None) -> None:
        self.model = model
        self.db = db
        self.fields = [f'{model.__name__}_id']
        append = False
        self.cur = cur
        
        for i in getmembers(model) :
            key = i[0]
            if append:
                self.fields.append(key)
            if key == '__weakref__':
                append = True

    def insert (self,**kwargs):
        """
            Insert into the database 
            with the fields where given 
            from kwargs
        """

        table = self.model.__name__

        keys = []
        values = []

        for key, val in kwargs.items() : 
            if type(val) != tuple : 
                keys.append(key)  
                values.append(val)
            else:
                keys.append(f'{val[0].__name__}_id')
                values.append(val[1])

        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(
            table,
            ','.join(keys),
            ','.join(["?" if self.db_type == 'sqlite3' else "%s" for i in range(len(values))]))



        if self.cur : 
            self.cur.execute(query, tuple(values))
        else:            
            self.db.execute(query, tuple(values))
        self.db.commit()
    
    def convert_to_dict (self, db_data) : 
        """
          convert the db output to dict
        """
        data = []

        current_data_index = 0
        
        while current_data_index < len(db_data) : 
            f_index = 0
            dic_data = {}
            for i in db_data[current_data_index] :
                dic_data[self.fields[f_index]] = i if type(i) == str or type(i) == int else str(i)
                f_index += 1

            data.append(dic_data)
            current_data_index += 1
        return data
    
    def all (self, beutify:bool=False) :
        """
          fetch all fields in the table
        """
        table = self.model.__name__
        query = f"SELECT * FROM {table};"
        
        if self.cur:
            self.cur.execute(query)
            db_data = self.cur.fetchall()
        else:
            db_data = self.db.execute(query).fetchall()

        data = self.convert_to_dict(db_data)

        response = data or []

        if beutify : 
            import json
            response = json.dumps(response,indent=4)

        return response

    def get (self, beutify:bool=False ,**kwargs) : 
        """
          for getting query by enterd parameter
        """
        if len(kwargs) > 1 :
            raise ValueError("too many entered values")
        
        data = [(key,val) for key, val in kwargs.items()][0]
        key, val = data[0], data[1]

        if key not in self.fields : 
            raise ValueError(f"'{key}' not found in fields for {self.model.__name__} model")
        
        table = self.model.__name__
    
        if val != None :
            k_and_v = f"{key}='{val}'"
        else:
            k_and_v = f"{key}=NULL"

        query = f"SELECT * FROM {table} WHERE {k_and_v};"
        if self.cur:
            self.cur.execute(query)
            db_result = self.cur.fetchall()
        else:
            db_result = self.db.execute(query).fetchall()

        if len(db_result) > 1 :
            raise ValueError("expected one result ,but there are many")
        
        __d = self.convert_to_dict(db_result)
        response = __d[0] if len(__d) == 1 else []

        if beutify : 
            import json
            response = json.dumps(response,indent=4)

        return response

    def filter (self,beutify:bool=False,**kwargs) : 
        """
          filtering data in the db
        """
        keys = [k for k in kwargs.keys()]
        values = [val for val in kwargs.values()]

        for key in keys :
            if key not in self.fields : 
                raise ValueError(f"'{key}' not found in fields for {self.model.__name__} model")
        
        del key

        table = self.model.__name__

        query = f"SELECT * FROM {table} WHERE "

        for i in range(len(keys)) : 
            try :
                has_next = keys[i+1]
            except IndexError:
                has_next = False

            key, val = keys[i], values[i]
            if val == None :
                query += f"{key}=NULL "
            else:
                query += f"{key}='{val}' "

            if has_next :
                query += "AND "

        query += ";"

        if self.cur :
            self.cur.execute(query)
            db_result = self.cur.fetchall()
        else:
            db_result = self.db.execute(query).fetchall()
        
        __d = self.convert_to_dict(db_result)
        
        response = __d
        if beutify : 
            import json
            response = json.dumps(response,indent=4)

        return response

    def delete (self,**kwargs) : 
        keys = [k for k in kwargs.keys()]
        values = [val for val in kwargs.values()]

        for key in keys :
            if key not in self.fields : 
                raise ValueError(f"'{key}' not found in fields for {self.model.__name__} model")
        
        del key

        table = self.model.__name__

        query = f"DELETE FROM {table} WHERE "
        for i in range(len(keys)) : 
            try :
                has_next = keys[i+1]
            except IndexError:
                has_next = False

            key, val = keys[i], values[i]
            if val == None :
                query += f"{key}=NULL "
            else:
                query += f"{key}='{val}' "

            if has_next :
                query += "AND "

        query += ";"
        
        if self.cur:
            self.cur.execute(query)
        else:
            self.db.execute(query)
        self.db.commit()

    def update_by_id(self, id:int, fields:tuple) : 
        """
          update field in db 
        """
        key,val = fields
        query = f"""UPDATE {self.model.__name__}
            SET {key}='{val}'
             where {self.model.__name__}_id={id};"""
        if self.cur:
            self.cur.execute(query)
        else:
            self.db.execute(query)
        self.db.commit()





class Fields :
    
    @staticmethod
    def String(max_len=225, 
               null=False,
               unique=False): 
        query = f"VARCHAR({max_len})"
        if null:
            query += ' NULL'
        if unique:
            query += ' UNIQUE'
        return query
    
    @staticmethod
    def Integer(default=0) : 
        query = f"INTEGER DEFAULT({default})"
        return query
        

    @staticmethod
    def Bool(default=False): 
        query = f"BOOLEAN DEFAULT {default}"
        return query
    
    @staticmethod
    def Date (auto_add_now=False,null=False) : 
        query = f"DATE"
        if auto_add_now :
            query += f" DEFAULT({datetime.now().date()})"
        if null : 
            query += ' NULL'
        return query
    

    @staticmethod
    def ForigenKey (table:object, on_delete:str=None) :
        obj_id = f"{table.__name__}_id"

        query = f"{obj_id} INTEGER,FOREIGN KEY(@KEY@) REFERENCES {table.__name__}({obj_id})"

        if on_delete :
            query +=  "ON DELETE " + on_delete
        
        return query

    class OnDelete:
        CASCADE = "CASCADE"
        
        