from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def naga(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.all().order_by('topic_name')
    LOT=Topic.objects.all()[0:2]
    LOT=Topic.objects.all().order_by('topic_name')[0:3]
    
    d={'LOT':LOT}
    return render(request,'naga.html',d)
def brock(request):
    WOT=webpage.objects.all()
    WOT=webpage.objects.filter(topic_name='cricket')
    WOT=webpage.objects.exclude(topic_name='cricket')
    WOT=webpage.objects.all().order_by(Length('topic_name').desc())
    WOT=webpage.objects.all().order_by(Length('topic_name'))
    d={'WOT':WOT}
    return render(request,'brock.html',d)
def beast(request):
    AOT=access.objects.all()
    d={'AOT':AOT}
    return render (request,'beast.html',d)  