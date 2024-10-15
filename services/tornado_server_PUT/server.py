import asyncio
import tornado
import json

from db import todo

class UpdateTodo(tornado.web.RequestHandler):
    def put(self, todo_id) : 
        self.set_header('Content-Type',"application/json")

        get_todo = todo.get(TodoTable_id=todo_id)
        if len(get_todo) == 0 :
            data = {
                'message' : 'todo not found for updating'
            }
            self._status_code = 404
        else:
            if self.request.body : 
                body = json.loads(self.request.body)

            try : 
                data = {
                    'message' : 'todo updated successfully'
                }
                todo.update_by_id(id=todo_id,fields=('text' , body['text']))
                self._status_code = 200
            except Exception as er: 
                data = {
                    'message' : f"an error accoured : {er}"
                }
                self._status_code = 400

        self.write(json.dumps(data))

def make_app():
    return tornado.web.Application([
        (r"/v1/update/([a-zA-Z0-9]+)/", UpdateTodo),
    ])

async def main():
    app = make_app()
    app.listen(5003)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())