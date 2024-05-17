from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('telaprincipal/', views.telaprincipal_dsm, name='telaprincipal_dsm'),
]
