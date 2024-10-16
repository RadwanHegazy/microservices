from rest_framework.views import APIView
import requests
from core.services import FLASK, FASTAPI
from rest_framework.response import Response

class GetTodos(APIView) : 

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

    def get(self, request) : 
        url = FLASK + "v1/get/"
        req = requests.get(url)
        print(req.url)
        return Response(req.json(), status=req.status_code)
    

class GetTodo(APIView) : 
    def get(self, request, todo_id) : 
        url = FASTAPI + f"v1/get/{todo_id}/"
        req = requests.get(url)
        return Response(req.json(), status=req.status_code)
    