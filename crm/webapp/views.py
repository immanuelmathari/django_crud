from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
# to logout and authenticate
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'webapp/index.html')


# Register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            # return redirect('')
    
    context = {'form' : form} # this helps us to render username,password from createUserForm to our template register.html. its called a context dictionary in django
    return render(request, 'webapp/register.html', context=context)

# login a user
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # the first one is for the database
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                #return redirect('')
    
    context = {'form2': form} #take data to login.html
    return render(request, 'webapp/my-login.html', context=context)
        
