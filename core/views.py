from django.shortcuts import render

from core.models import Bucket

def Homepageview(request):
	obj = Bucket.objects.all()

	
	return render(request,'home.html',{'a1':obj})
# Create your views here.
def save(request):
	title=request.POST.get("title")
	movie=request.POST.get("movie")
	romance=request.POST.get("romance")
	action=request.POST.get("action")
	Bucket.objects.create(title=title,movie=movie,romance=romance,action=action)

	return render(request,'res.html')
