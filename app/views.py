from django.shortcuts import render
from app.models import *
# Create your views here.
def naga(request):
    LOT=Topic.objects.all()
    d={'LOT':LOT}
    return render(request,'naga.html',d)
def brock(request):
    WOT=webpage.objects.all()
    d={'WOT':WOT}
    return render(request,'brock.html',d)