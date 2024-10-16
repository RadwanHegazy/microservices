from rest_framework.views import APIView
import requests
from core.services import FALCON
from rest_framework.response import Response


class DeleteTodo(APIView) : 

    def delete(self, request, todo_id) : 
        url = FALCON + f"v1/delete/{todo_id}/"
        req = requests.delete(url)
        return Response(req.json(), status=req.status_code)