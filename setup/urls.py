from django.contrib import admin
from django.urls import path
from encurtador.views import criar_link_curto, redirecionar_link
from django.contrib import admin
from django.urls import path
from encurtador.views import pagina_inicial

urlpatterns = [
    path('', pagina_inicial),
    path('admin/', admin.site.urls),
    path('api/encurtar/', criar_link_curto),
    path('<str:codigo>/', redirecionar_link),
]
