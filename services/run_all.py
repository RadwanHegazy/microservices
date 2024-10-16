import threading, os


def flask():
    os.system("py flask_server_GET/server.py")

def fastapi():
    os.system("cd fastapi_server_GET_RETRIVE && fastapi dev server.py --port=5001")

def falcon() : 
    os.system("py falcon_server_DELETE/server.py")

def tornado() : 
    os.system("py tornado_server_PUT/server.py")

def bottle():
    os.system("py bottle_server_POST/server.py")


th_flask = threading.Thread(target=flask)
th_fastapi = threading.Thread(target=fastapi)
th_falcon = threading.Thread(target=falcon)
th_tornado = threading.Thread(target=tornado)
th_bottle = threading.Thread(target=bottle)

th_flask.start()
th_fastapi.start()
th_falcon.start()
th_tornado.start()
th_bottle.start()
