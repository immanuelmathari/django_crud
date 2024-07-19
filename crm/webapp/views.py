from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

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
    
    context = {'form' : form} # this helps us to render username,password from createUserForm to our template register.html
    return render(request, 'webapp/register.html', context=context)
    
