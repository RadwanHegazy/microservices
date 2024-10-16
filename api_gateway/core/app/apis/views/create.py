from rest_framework.views import APIView
import requests
from core.services import BOTTLE
from rest_framework.response import Response
from ..serializers import TodoSerializer

class CreateTodo (APIView) : 
    serializer_class = TodoSerializer

    def post(self, request) : 
        url = BOTTLE + "v1/create/"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() : 
            req = requests.post(url,json={
                'text' : request.data.get('text')
            } )
            return Response(req.json(), status=req.status_code)
        return Response(serializer.errors, status=400)