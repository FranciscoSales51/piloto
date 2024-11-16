from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<p>A view index funcionou, Wow!</p>")
    return render(request, 'home/index.html')


def sobre(request):    
    # return HttpResponse('Sobre o sistema')
    return render(request,'home/sobre.html')

def contato(request):
    return render(request,'home/contato.html')

def exibir_item(request, id):
    return render(request,'home/exibir-item.html', {'id': id})

def perfil(request, usuario):
    return render(request,'home/perfil.html', {'usuario': usuario})


def diasemana(request, dia):
    # Dicionário para mapear os dias da semana
    dias_semana = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado",
    }
    
    # Verifica se o número está no intervalo válido
    if 1 <= dia <= 7:
        mensagem = f"O dia selecionado é {dias_semana[dia]}."
    else:
        mensagem = "Erro: Insira um número entre 1 e 7."
    
    # Define o contexto com a mensagem
    context = {
        "mensagem": mensagem
    }
    
    # Renderiza a página com o contexto
    return render(request, 'home/dia-semana.html', context)

