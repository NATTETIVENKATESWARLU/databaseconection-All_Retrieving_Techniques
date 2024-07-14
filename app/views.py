from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length 
# Create your views here.



def topic(request):
    topic=Topic.objects.all()
    to={"topic":topic}
    return render(request,'topic.html',to)

def webpage(request):
    web=Webpage.objects.all()
    web=Webpage.objects.filter(topic_name="kabbadi")
    web=Webpage.objects.filter(name__regex='R\w+')
    web=Webpage.objects.filter(Q(name='venkey') | Q(url__startswith='https'))
    web=Webpage.objects.filter(Q(name='venkey') & Q(url__startswith='http'))
    web=Webpage.objects.order_by("name")
    web=Webpage.objects.order_by("topic_name")
    web=Webpage.objects.order_by(Length("name"))
    web=Webpage.objects.all()[0:5]
    web=Webpage.objects.order_by("-topic_name")
    LOW=Webpage.objects.filter(name__startswith='k')
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__contains='S')
    LOW=Webpage.objects.filter(name__in=('ashu','yAsh'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    d={"LOW":LOW}
    return render(request,"webpage.html",d)


def accessrecord(request):
    LOA=Aceess_records.objects.all()
    LOA=Aceess_records.objects.filter(date__gt='2022-10-10')
    LOA=Aceess_records.objects.filter(date__gte='2022-10-10')
    LOA=Aceess_records.objects.filter(date__lt='2022-10-10')
    LOA=Aceess_records.objects.filter(date__lte='2022-10-10')
    LOA=Aceess_records.objects.filter(date__year='2023')
    LOA=Aceess_records.objects.filter(date__month='10')
    LOA=Aceess_records.objects.filter(date__day='5')
    LOA=Aceess_records.objects.filter(date__year__gt='2023')
    LOA=Aceess_records.objects.filter(date__month__lt='10')
    LOA=Aceess_records.objects.all()
    LOA=Aceess_records.objects.filter(date__day='7')
    
    d={'access':LOA}

    return render(request,"accessrecord.html",d)
    
