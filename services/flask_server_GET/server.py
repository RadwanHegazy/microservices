from flask import Flask, jsonify
from db import db, TodoTable

app = Flask(__name__)

@app.get("/v1/get/")
def get_all_data() : 
    db.create_table(TodoTable)
    todo = db.manage(TodoTable)
    return jsonify(todo.all()), 200

if __name__ == "__main__" : 
    app.run(
        port=5000
    )