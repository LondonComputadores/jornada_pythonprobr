from django.shortcuts import render
from quiz.base.models import Pergunta


def home(requisicao):
    return render(requisicao, 'base/home.html')

def end(requisicao):
    return render(requisicao, 'base/end.html')

def perguntas(requisicao, indice):
    pergunta = Pergunta.objects.filter(disponível=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(requisicao, 'base/game.html', context=contexto)


