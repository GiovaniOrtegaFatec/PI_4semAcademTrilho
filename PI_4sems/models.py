from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
# Create your models here.

class Task(models.Model):
    curso = models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    diasemana = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    sala = models.CharField(max_length=100)

    def __str__(self):
        return self.curso,self.semestre,self.diasemana,self.horario,self.materia,self.professor,self.sala
    
