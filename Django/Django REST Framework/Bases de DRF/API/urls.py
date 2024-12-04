from django.urls import include, path
from .views import TaskView, TaskViewXML, TaskViewSet, CustomAuthToken
from rest_framework import routers
from rest_framework.authtoken import views

# Importamos las librerías necesarias para usar YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)

# Añadimos el schema para la documentación de nuestra API
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='Tasklist'),
    path('tasks/<int:pk>', TaskView.as_view(), name='Tasks_details'),
    path('tasks-xml/', TaskViewXML.as_view()),
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token)
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]