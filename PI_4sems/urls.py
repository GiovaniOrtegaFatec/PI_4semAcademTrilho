from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('telaprincipal/', views.telaprincipal, name='telaprincipal'),
    path('gradecurricular/', views.grade_curricular, name='grade_curricular'),
]
