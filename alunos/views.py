import json
from django import forms 
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import require__http_methods
from .models import Aluno

Class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "turma", "nota"]

def index(request):
    return render(request, "index.html")        

# Create your views here.
