from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('recetas.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Administrador(models.Model):
    Name = models.CharField(max_length=250)
    rutADM = models.CharField(primary_key=True,max_length=12)
    emailadm = models.EmailField('User Mail' ,max_length=250)

class Cliente(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=250)
    email = models.EmailField('User Mail' ,max_length=250)
    fono = models.IntegerField
    useradm = models.ForeignKey(Administrador, on_delete = models.CASCADE)



class Recetas(models.Model):
    fotoRece = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    ingrediente = models.TextField(max_length=500)
    pasos = models.TextField(max_length=500)
    id = models.TextField(primary_key=True,max_length=12)
    admimg = models.ForeignKey(Administrador, on_delete = models.CASCADE)

class RecePremium(models.Model):
    Video = models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    ingre = models.TextField(max_length=500)
    pasosvidio = models.TextField(max_length=500)
    idvidio = models.TextField(max_length=12)
    admvid = models.ForeignKey(Administrador, on_delete = models.CASCADE)
# Create your models here.
