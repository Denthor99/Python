from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'published') # Modifica la vista del modelo (Post)
    list_filter = ['published'] # Añade filtrado
    search_fields = ['title', 'body'] # Añade búsqueda
    prepopulated_fields = {'slug':('title',)} # Genera el slug de forma automatica