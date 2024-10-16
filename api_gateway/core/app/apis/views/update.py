from rest_framework.views import APIView
import requests
from core.services import TORNADO
from rest_framework.response import Response
from ..serializers import TodoSerializer


class UpdateTodo(APIView) : 
    serializer_class = TodoSerializer

    def put(self, request, todo_id) : 
        url = TORNADO + f"v1/update/{todo_id}/"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() : 
            req = requests.put(url, json={
                'text' : request.data.get('text')
            })
            return Response(req.json(), status=req.status_code)
        return Response(serializer.errors, status=400)