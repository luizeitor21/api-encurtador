from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from .models import Link
from django.shortcuts import render

# Create your views here.
@api_view(['POST'])
def criar_link_curto(request):
    url = request.data.get('url_original')
    if not url:
        return Response({"erro": "Envie a url_original"}, status=400)
    
    novo_link = Link.objects.create(url_original=url)
    
    link_curto = f"http://127.0.0.1:8000/{novo_link.codigo}"
    
    return Response({"url_curta": link_curto, "codigo": novo_link.codigo})

def redirecionar_link(request, codigo):
    link_salvo = get_object_or_404(Link, codigo=codigo)
    return redirect(link_salvo.url_original)

def pagina_inicial(request):
    return render(request, 'index.html')