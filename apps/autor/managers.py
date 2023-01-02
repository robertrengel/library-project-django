from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    #manager para el modelo autor

    #def listar_autores(self):
    #    return self.all()

    def buscar_autor(self, kword):
        return self.filter(firts_name__icontains=kword)

    def buscar_autor2(self, kword):
        return self.filter(firts_name__icontains=kword) | self.filter(last_name__icontains=kword)

    def buscar_autor3(self, kword):
        return self.filter(firts_name__icontains=kword).exclude(Q(age__icontains=83) | Q(age__icontains=67))

    def buscar_autor4(self, kword):
        return self.filter(age__gt=43, age__lt=68)
        
