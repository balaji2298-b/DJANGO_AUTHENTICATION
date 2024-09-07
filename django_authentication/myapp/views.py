from django.shortcuts import render
from myapp.models import Hello


def index(request):
	if request.method == 'POST':
		hello = Hello(name=request.POST['name'],username=request.POST['username'],password=request.POST['password'])
		hello.save()
		return render(request,'index.html')
	else:
	    return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def nice(request):
	if request.method == 'POST':
		if Hello.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
			request.session['a']=request.POST['username']
			return render(request,'nice.html')
		else:
			context = {'msg': 'Invalid username or password'}
			return render(request,'login.html',context)

