from django.shortcuts import render
from myapp.models import Hello
from django.contrib import messages

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

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']
        try:
            user = Hello.objects.get(username=username)
            user.password = new_password
            user.save()
            messages.success(request, 'Password successfully changed!')
            return redirect('login')  # Assuming 'login' is the name of your login URL
        except Hello.DoesNotExist:
            return render(request, 'forgotpassword.html', {'msg': 'Username not found'})
    return render(request, 'forgotpassword.html')

