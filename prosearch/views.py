from django.shortcuts import render
from prosearch import models
from django.shortcuts import render_to_response

def index(request):
    return render(request,"index.html",)
# Create your views here.

def searchpro(request):
    if request.method=="POST":
        proname=request.POST.get("name",None)
        q1=models.Person.objects.filter(name__icontains=proname)
        return render(request,"result.html",{"data":q1})



def searchfield(request):
    if request.method=="POST":
        area=request.POST.get("field",None)
        p=models.Field.objects.filter(area__icontains=area)
        p1=[]

        for m in p:
            p1+=models.Person.objects.filter(name__contains=m)
        return render(request,"result.html",{"data":p1})
