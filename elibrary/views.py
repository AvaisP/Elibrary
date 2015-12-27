from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserFormRegister, UserForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def testview(request):
	return render(request,'base.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        users_form = UserFormRegister(data = request.POST)
        if user_form.is_valid() and users_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            userregister = users_form.save(commit=False)
            userregister.user = user
            userregister.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, new_user)
            return redirect('/allbooks/')
    else:
        user_form = UserForm()
        users_form = UserFormRegister()
    return render(request, 'register.html',{'user_form':user_form, 'users_form':users_form},)  	

def login_library(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/allbooks/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'login.html',)

@login_required
def logout_library(request):
    logout(request)
    return redirect('/')

def allbooks(request):
    ID = [1,2]
    bookName = ["Python", "Java"]
    author = ["idk", "who"]
    copies = [3,7]
    books = zip(ID, bookName, author, copies)
    return render(request, 'allbooks.html',{'books':books})

def availbooks(request):
    ID = [1,2]
    bookName = ["Python", "Java"]
    author = ["idk", "who"]
    copies = [3,0]
    books = zip(ID, bookName, author, copies)
    return render(request, 'availbooks.html',{'books':books})

