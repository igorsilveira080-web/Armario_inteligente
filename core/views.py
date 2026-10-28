from django.shortcuts import render
from django.http import JsonResponse
from .utils import buscar_status_nicho_banco
from django.db import connection
from 

# Create your views here.
def index(request):
    context = {
        'titulo':'Armario de Chaves',
        'Nome':'Igor Silveira',

    }
    return render(request,'index.html', context)

def status_nicho_view(request):
    #1. Conexão e execução 
    with connection.cursor() as cursor: 
        cursor.execute("SELECT * FROM vw_status_nicho")
    
        #2. Transformação 
        dados_nichos = dictfetchall(cursor)
    nichos = buscar_status_nicho_banco()
    return JsonResponse (nichos, safe=False, status=200)



