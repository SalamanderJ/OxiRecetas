from django.contrib import admin
from .models import Post, Comment
from .models import Administrador
from .models import Cliente
from .models import Recetas
from .models import RecePremium
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Administrador)
admin.site.register(Cliente)
admin.site.register(Recetas)
admin.site.register(RecePremium)
