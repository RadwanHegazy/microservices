from flask import Flask
from db import todo

app = Flask(__name__)


@app.get("/v1/get/")
def get_all_data() : 
    todos = todo.all()
    return todos, 200

if __name__ == "__main__" : 
    app.run(
        port=5000
    )