#from django.contrib.auth.decorators import login_required
from .models import Contacto

def cantidad_mensajes(request):
    return {'cantidad_mensajes': Contacto.objects.count()}

def lista_mensajes(request):
    mensajes = Contacto.objects.all().order_by("-enviado")[:5]
    return {'mensajes': mensajes}