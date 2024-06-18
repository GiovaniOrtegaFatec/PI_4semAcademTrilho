from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from PI_4sems.models import Task

data_atual = datetime.now()
dia_da_semana_numero = data_atual.weekday()
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
dias_da_semana1= ["SEG","TER","QUA","QUI","SEX","SAB","DOM"]
dia_da_semana = dias_da_semana[dia_da_semana_numero]
dia_da_semana1= dias_da_semana1[dia_da_semana_numero]
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")

def index(request):
    return  render(request, 'PI_4sems/index.html')

def telaprincipal(request):
    if request.method == 'POST':
        curso = request.POST.get('curso')
        semestre = request.POST.get('semestre')
        print('CURSO    POST:', curso)
        print('SEMESTRE POST: ', semestre)
        # Processamento...
        print("Data:", data_formatada)
        print("Dia da semana:", dia_da_semana)
        print("Dia da semana:", dia_da_semana1)
        tasks_curso = Task.objects.filter(curso=curso,semestre=semestre,diasemana=dia_da_semana1).first()
        if tasks_curso:
            return render(request, 'PI_4sems/TelaPrincipal.html', {'tasks_curso': tasks_curso, 'data': data_formatada, 'dia': dia_da_semana})
        else:
            return HttpResponse('Nenhuma tarefa encontrada para os critérios fornecidos.')
    elif request.method == 'GET':
        # Processamento para requisição GET, se necessário.
        return render(request, 'PI_4sems/TelaPrincipal.html')
    else:
        return HttpResponse('Método não permitido')

def grade_curricular(request):
    if request.method == 'POST':
        curso = request.POST.get('curso')
        semestre = request.POST.get('semestre')
        print('CURSO    POST: ', curso)
        print('SEMESTRE POST: ', semestre)
        
        # Processamento...
        tasks = Task.objects.filter(curso=curso, semestre=semestre)
        return render(request, 'PI_4sems/grade_curricular.html', {'tasks': tasks})
    else:
        return HttpResponse('Método não permitido')


def mapa(request):
    if request.method == 'POST':
        curso = request.POST.get('curso')
        semestre = request.POST.get('semestre')
        print('CURSO    POST: ', curso)
        print('SEMESTRE POST: ', semestre)
        
        # Processamento...
        tasks_mapa = Task.objects.filter(curso=curso, semestre=semestre,diasemana=dia_da_semana1).first()
        print('SALA: ', tasks_mapa.sala+'.jpg')
        sala_mapa = tasks_mapa.sala+'.jpg'
        print('SALA: ', sala_mapa)
        return render(request, 'PI_4sems/mapa.html', {'tasks_mapa': tasks_mapa, 'sala_mapa': sala_mapa})
    else:
        return HttpResponse('Método não permitido')


