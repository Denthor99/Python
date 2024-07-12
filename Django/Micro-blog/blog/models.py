from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    published = models.BooleanField(default=False)

    # Con esto mostramos el titulo en el apartado admin de Django
    def __str__(self) -> str:
        return self.title