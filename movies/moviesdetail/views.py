from unittest import result
from django.shortcuts import render
from moviesdetail.models import Movi

def showdata(request):
    results = Movi.objects.all()
    return render(request, 'index.html', {"data":results})