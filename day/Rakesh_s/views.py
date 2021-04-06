from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<style>h1{ text-align:center;} h1</style><h1 style='color:white;background-color:red'>this is home page</h1>")

def chk(request):
	return HttpResponse("<script> alert('hi good')</script><h1>welll done</h1>")

def home(request):
	return render(request,'bt/home.html')

def login(re):
	return render(re,'bt/login.html')

def register(rt):
	return render(rt,'bt/register.html')

def bthm(q):
	return render(q,'bt/bthome.html')
def rg(r):
	if r.method=="POST":
		emailID=r.POST['email']
		password=r.POST['pswd']
		age=r.POST['age']
		return render(r,'bt/home.html',{'person_email':emailID,'password':password})
	return render(r,'bt/rg.html')

 
