from bottle import Bottle, run, response, request
import json
from db import todo

app = Bottle()



@app.route('/v1/create/', method=['POST'])
def handle_item():
    body = request.json
    response.content_type = "application/json"
    todo_text = body.get('text', '')
    
    if todo_text == '':
        response.status = 400
        return json.dumps({
            'message' : 'please insert todo text'
        })
    
    todo.insert(text=todo_text)
    response.status = 201
    data = {
        'message' : 'todo created successfully'
    }
    return json.dumps(data)

if __name__ == '__main__':
    run(app, host='localhost', port=5004)