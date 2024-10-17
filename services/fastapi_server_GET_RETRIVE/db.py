from radwan_orm.orm import RadwanORM, Fields
Fields = Fields.Fields


# db configuration
config = {
    "NAME":"microservice",
    "HOST":"localhost",
    "PASSWORD":"admin",
    "USER":"root",
}

db = RadwanORM()
db = db.connect(
    dbtype='mysql',
    config=config 
)

class TodoTable :
    text = Fields.String(max_len=300, null=False)

