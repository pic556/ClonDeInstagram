from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pub_instagram(models.Model):
    usuario = models.ForeignKey(
        User , on_delete=models.CASCADE,related_name="post",null=True)
    #image = models.ImageField()
    likes = models.PositiveIntegerField(default = 0 , blank=True)
    fecha_pub = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.descripcion

class Com_instagram(models.Model):
    texto = models.TextField()
    postear = models.ForeignKey(
        Pub_instagram, on_delete=models.CASCADE,related_name="comments", null=True)
    usuario = models.ForeignKey(
        User , on_delete=models.CASCADE,related_name="comments", null=True)

    def __str__(self):
        return self.texto
