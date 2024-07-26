from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    nivel = models.CharField(max_length=50)
    enlace = models.URLField(max_length=200)
    resumen = RichTextField()  # Usamos RichTextField para permitir HTML y CKEditor
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)  # Campo para la imagen

    def __str__(self):
        return self.titulo
