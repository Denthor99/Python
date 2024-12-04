from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.http import HttpResponse
from django.template import loader
from django.utils.timezone import datetime
import re
from maintenance_mode.decorators import force_maintenance_mode_off

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@force_maintenance_mode_off
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")

    # Filtro name con Regex
    match_object = re.match("[a-zA-Z]+", name)
    clean_name = match_object.group(0) if match_object else "Amigo"
    content = f"¡Muy buenas, {clean_name}! Hoy es {formatted_now}"
    return HttpResponse(content)