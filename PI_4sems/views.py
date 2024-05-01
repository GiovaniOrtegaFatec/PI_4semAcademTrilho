from django.shortcuts import render

def index(request):
    """Página principal do PI_4sem"""
    return  render(request, 'PI_4sems/index.html')
