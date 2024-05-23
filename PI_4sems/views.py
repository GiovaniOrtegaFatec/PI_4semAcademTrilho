from django.shortcuts import render

def index(request):
    """Página principal do PI_4sem"""
    return  render(request, 'PI_4sems/index.html')

def telaprincipal(request):
    return render(request, 'PI_4sems/TelaPrincipal.html')

def grade_curricular(request):
    return render(request, 'PI_4sems/grade_curricular.html')

def mapa(request):
    return render(request, 'PI_4sems/mapa.html')
