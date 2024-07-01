from django.db import models

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
"""

class PRODUCTO (models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/')

