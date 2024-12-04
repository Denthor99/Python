from typing import Any
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Task

import json

# Importamos todo lo necesario para deshabilitar el CSRF
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Importamos los serializadores
from django.core import serializers
from rest_framework import viewsets
from .serializers import TaskSerializer

# Importamos los paquetes necesarios para la autenticacion
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Importamos los paquetes necesarios para los tokens
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

class TaskView(View):

    # Definimos una función que deshaiblitará usar CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk=0):
        if (pk > 0):
            tasks = list(Task.objects.filter(id=pk).values())
            if tasks:
                task = tasks[0]
                datos = { 'message': 'Todo correcto', 'Tarea': task}
        else:   
            tasks = list(Task.objects.values())
            if tasks:
                datos = { 'message': 'Todo correcto', 'Tareas': tasks}
            else:
                datos = {'message': 'No hay tareas'}

        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Task.objects.create(title=jd['title'], 
                            description=jd['description'], 
                            complete=jd['complete'])
        datos = {'message': 'Tarea creada correctamente.'}
        return JsonResponse(datos)
    
    def put(self, request, pk=0):
        jd = json.loads(request.body)
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
                task = Task.objects.get(id=pk)
                task.title = jd['title']
                task.description = jd['description']
                task.complete = jd['complete']
                task.save()
                datos = {'message': 'Tarea actualizada correctamente.'}
        else:
            datos = {'message': 'No hay tarea con ese ID.'}
        return JsonResponse(datos)

    def delete(self, request, pk=0):
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            Task.objects.filter(id=pk).delete()
            datos = {'message': 'Tarea eliminada correctamente.'}
        else:
            datos = {'message': 'No hay tarea con ese ID.'}
        return JsonResponse(datos)
    
class TaskViewXML(View):
    def get(self, request):
        data = serializers.serialize('xml', Task.objects.all())
        return HttpResponse(data)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

# Creamos una clase que nos devolverá un json con el id, el token y el email del usuario
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })