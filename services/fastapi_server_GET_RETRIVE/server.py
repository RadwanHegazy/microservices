from fastapi import FastAPI
from db import todo
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/v1/get/{todo_id}/")
def get_todo (todo_id) : 
    get_todo = todo.get(TodoTable_id=todo_id)
    if len(get_todo) == 0:
        return JSONResponse({
            'message' : "todo not found"
        }, status_code=404)
        
    return JSONResponse(get_todo, status_code=200)

