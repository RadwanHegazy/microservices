import falcon
import json

from db import todo

class DeleteTodo:
    
    def on_delete(self, req, resp, todo_id) :
        get_todo = todo.get(TodoTable_id=todo_id)
        if len(get_todo) == 0 : 
            resp.status = falcon.HTTP_404
            resp.media = {
                'message' : 'todo not found'
            }
        else:
            todo.delete(TodoTable_id=todo_id)
            resp.status = falcon.HTTP_200
            resp.media = {
                'message' : 'todo deleted successully'
            }
        
app = falcon.App()
app.add_route('/v1/delete/{todo_id}/', DeleteTodo())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    with make_server('localhost', 5002, app) as httpd:
        print("[+] Falcon Server is Running ..")
        print("[+] Serving on http://localhost:5002")
        httpd.serve_forever()