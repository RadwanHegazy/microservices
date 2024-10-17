from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from frontend.settings import GATEWAY_URL
import requests
from django.http import Http404


class GetTodos(TemplateView) : 
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Get the todos from the gateway

        Returns:
            dict[str, Any]: all todos data
        """
        res = requests.get(
            url=GATEWAY_URL + "/todo/v1/get/"
        )
        return {
            'todos' : res.json()
        }
    
    def post(self, request) : 
        res = requests.post(
            url=GATEWAY_URL + "/todo/v1/create/",
            data={
                'text' : request.POST.get('text')
            }
        )
        return redirect('home')
    
class UpdateTodo(TemplateView) :
    template_name = 'update.html'

    def get(self, request, todo_id) :
        """Get the todo by id

        Args:
            request (Object): request data
            todo_id (Int): the id of todo

        Returns:
            _type_: template file
        """
        context = {}
        res = requests.get(
            url=GATEWAY_URL + f"/todo/v1/get/{todo_id}/"
        )

        print(res.json())

        if res.status_code == 404 :
            raise Http404(request)
        
        context['todo'] = res.json()
        return render(request, self.template_name, context)
    

    def post(self, request, todo_id) :
        """Update todo depends on incoming data

        Args:
            request (Object): client request
            todo_id (Int): the id of todo

        Returns:
            _type_: redirect to the todos home
        """
        res = requests.put(
            url=GATEWAY_URL + f"/todo/v1/update/{todo_id}/",
            data={
                'text' : request.POST.get('text')
            }
        )
    
        if res.status_code == 404 :
            raise Http404(request)
        
        return redirect('home')
    

class DeleteTodo(RedirectView) : 
    def get (self, request, todo_id) : 
        """Delete todo by id

        Args:
            request (_type_): _description_
            id (_type_): _description_

        Returns:
            _type_: redirect to home page
        """
        res = requests.delete(
            url=GATEWAY_URL + f"/todo/v1/delete/{todo_id}/",
        )

        if res.status_code == 404:
            raise Http404(request)
        
        return redirect("home")