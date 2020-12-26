# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'umtemplate.html'
    contexto = {
        'titulo': 'Lazy Studant',
        'subtitulo': 'View simples para mostrar como utilizar templates',
        'texto': 'O Objetivo desse sistema é ensinar como utilizar template filter, tags, for e if para novatos em aprendizado do django. O foco será templates',
        'cities': [
            {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
            {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
            {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
            {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
            {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
        ]
    }
    return render(request, template, contexto)