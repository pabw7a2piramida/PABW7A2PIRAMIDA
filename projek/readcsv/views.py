from django.shortcuts import render
from .rscv import *

def index(request):
    return render(request, 'index.html', {'rows':rows})
