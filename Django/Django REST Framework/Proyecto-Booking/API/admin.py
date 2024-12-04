from django.contrib import admin
from .models import Resource, Booking
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(Booking)
admin.site.register(Resource)
TokenAdmin.raw_id_fields = ['user']