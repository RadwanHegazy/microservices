from django.test import TestCase
from django.urls import reverse

class TestTodoEndpoints (TestCase):

    def test_get_all_todos(self) : 
        response = self.client.get(reverse("get_todos"))
        self.assertEqual(response.status_code, 200)

    def test_create_todo_failed(self):
        response = self.client.post(reverse('create_todo'))
        self.assertNotEqual(response.status_code, 200)

    def test_get_undefined_todo(self) : 
        response = self.client.get(reverse('get_todo', args=[100]))
        self.assertNotEqual(response.status_code, 200)

    def test_create_todo_success(self) : 
        response = self.client.post(reverse("create_todo"), data={
            'text' : "test todo"
        }, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_get_todo_success(self) :
        response = self.client.get(reverse('get_todo', args=[3]))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_undefined_todo(self):
        response = self.client.get(reverse('delete_todo', args=[1]))
        self.assertNotEqual(response.status_code, 200)
        
    def test_update_undefined_todo(self):
        response = self.client.get(reverse('update_todo', args=[1]))
        self.assertNotEqual(response.status_code, 200)
    

