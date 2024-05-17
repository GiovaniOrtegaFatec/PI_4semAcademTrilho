from django.shortcuts import render

def index(request):
    """Página principal do PI_4sem"""
    return  render(request, 'PI_4sems/index.html')

def telaprincipal_dsm(request):
    return render(request, 'PI_4sems/TelaPrincipal_DSM.html')
