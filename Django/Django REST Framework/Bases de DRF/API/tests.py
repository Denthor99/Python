from django.test import TestCase

# Importamos librerías que nos harán falta más adelante
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.

class TaskAPITestCase(APITestCase):
    fixtures = ['tasks.json', 'user.json']
    def _authenticate(self):
        usuario = User.objects.get(username="admin")
        token = Token.objects.create(user=usuario)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ token.key)

    def test_get_task(self):
       
        # Task.objects.create(title=f'tarea n1', description=f'descripcion n1', complete=False)
        # Task.objects.create(title=f'tarea n2', description=f'descripcion n2', complete=False)

        # Nos autenticamos usando la función
        self._authenticate()

        response = self.client.get('/api/tareas/')
        response_json = response.json()
        # print(response_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 2)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)
        self.assertIsInstance(response_json[1], dict)
    
    def test_post_tasks(self):
        self._authenticate()
        url = '/api/tareas/'
        data = {'title': 'Test Task', 'description': 'Test Description', 'complete': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


