from django.shortcuts import render
from django.http import HttpResponse
from .models import Proo
from .forms import Proo_form

def home(request):
	nam = Proo.objects.all()
	return render(request,'result.html',{'ab':nam})


def proo_view(request):
	
	return render(request,'prod_cre.html')


def su_b(request):
	a1=request.POST.get("name")
	a2=request.POST.get("descrip")
	a3=request.POST.get("dindong")
	a4=request.POST.get("hhgh")
	a5=request.POST.get("real")

	Proo.objects.create(name=a1,descrip=a2,dindong=a3,hhgh=a4,real=a5)
	return render(request,'res.html')
