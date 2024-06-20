from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from PI_4sems.models import Task

data_atual = datetime.now()
dia_da_semana_numero = data_atual.weekday()
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
dias_da_semana1 = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
dia_da_semana = dias_da_semana[dia_da_semana_numero]
dia_da_semana1 = dias_da_semana1[dia_da_semana_numero]
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")

def index(request):
    return render(request, 'PI_4sems/index.html')

def telaprincipal(request):
    if request.method == 'POST':
        curso = request.POST.get('curso')
        semestre = request.POST.get('semestre')
        request.session['curso'] = curso
        request.session['semestre'] = semestre
        print('CURSO    POST:', curso)
        print('SEMESTRE POST:', semestre)
        print("DATA.........:", data_formatada)
        print("DIA DA SEMANA:", dia_da_semana)
        print("DIA DA SEMANA:", dia_da_semana1)
        # Processamento...
        if not curso or not semestre:
           return HttpResponse('Curso e semestre não definidos.')        
        tasks_curso = Task.objects.filter(curso=curso, semestre=semestre, diasemana=dia_da_semana1).first()
        if tasks_curso:
            request.session['materia'] = tasks_curso.materia
            request.session['professor'] = tasks_curso.professor
            request.session['sala'] = tasks_curso.sala
            return render(request, 'PI_4sems/TelaPrincipal.html', {
                'curso': curso,
                'semestre': semestre,
                'materia': tasks_curso.materia,
                'professor': tasks_curso.professor,
                'sala': tasks_curso.sala,
                'data': data_formatada,
                'dia': dia_da_semana
            })
        else:
            return HttpResponse('Nenhuma tarefa encontrada para os critérios fornecidos.')
    elif request.method == 'GET':
        curso = request.session.get('curso')
        semestre = request.session.get('semestre')
        materia = request.session.get('materia')
        professor = request.session.get('professor')
        sala = request.session.get('sala')
        print('CURSO    SESSION:', curso)
        print('SEMESTRE SESSION:', semestre)
        print('MATERIA  SESSION:', materia)
        print('PROFESSOR SESSION:', professor)
        print('SALA SESSION:', sala)
        # Processamento para requisição GET, se necessário.
        return render(request, 'PI_4sems/TelaPrincipal.html', {
            'curso': curso,
            'semestre': semestre,
            'materia': materia,
            'professor': professor,
            'sala': sala,
            'data': data_formatada,
            'dia': dia_da_semana
        })
    else:
        return HttpResponse('Método não permitido')

def grade_curricular(request):
    curso = request.session.get('curso')
    semestre = request.session.get('semestre')
    materia = request.session.get('materia')
    professor = request.session.get('professor')
    sala = request.session.get('sala')
    print('CURSO    SESSION:', curso)
    print('SEMESTRE SESSION:', semestre)
    print('MATERIA  SESSION:', materia)
    print('PROFESSOR SESSION:', professor)
    print('SALA SESSION:', sala)
    if not curso or not semestre:
        return HttpResponse('Curso e semestre não definidos.')
    tasks = Task.objects.filter(curso=curso, semestre=semestre)
    return render(request, 'PI_4sems/grade_curricular.html', {
        'tasks': tasks,
        'curso': curso,
        'semestre': semestre,
        'materia': materia,
        'professor': professor,
        'sala': sala
    })

def mapa(request):
    curso = request.session.get('curso')
    semestre = request.session.get('semestre')
    materia = request.session.get('materia')
    professor = request.session.get('professor')
    sala = request.session.get('sala')
    print('CURSO    SESSION:', curso)
    print('SEMESTRE SESSION:', semestre)
    print('MATERIA  SESSION:', materia)
    print('PROFESSOR SESSION:', professor)
    print('SALA SESSION:', sala)
    if not curso or not semestre:
        return HttpResponse('Curso e semestre não definidos.')
    tasks_mapa = Task.objects.filter(curso=curso, semestre=semestre, diasemana=dia_da_semana1).first()
    if tasks_mapa:
        sala_mapa = tasks_mapa.sala + '.jpg'
        return render(request, 'PI_4sems/mapa.html', {
            'tasks_mapa': tasks_mapa,
            'sala_mapa': sala_mapa,
            'curso': curso,
            'semestre': semestre,
            'materia': materia,
            'professor': professor,
            'sala': sala
        })
    else:
        return HttpResponse('Nenhuma tarefa encontrada para os critérios fornecidos.')
