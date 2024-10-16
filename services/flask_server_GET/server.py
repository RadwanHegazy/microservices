from flask import Flask, jsonify
from db import todo

app = Flask(__name__)

@app.get("/v1/get/")
def get_all_data() : 
    return jsonify(todo.all()), 200

if __name__ == "__main__" : 
    app.run(
        port=5000
    )