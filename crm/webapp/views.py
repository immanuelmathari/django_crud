from django.shortcuts import render, redirect
from django.http import HttpResponse
# to logout and authenticate
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
# to make sure only authenticated users access restricted pages
from django.contrib.auth.decorators import login_required
from . models import Record
from . forms import CreateRecordForm, UpdateRecordForm, CreateUserForm, LoginForm
from django.contrib import messages

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
            messages.success(request, "Account created successfully!")
            return redirect('my-login')
    
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
                messages.success(request, "Logged in!")
                return redirect('dashboard')
    
    context = {'form2': form} #take data to login.html
    return render(request, 'webapp/my-login.html', context=context)

# - Dashboard view
@login_required(login_url='my-login') # ensures that only authorized users access dashboard
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records' : my_records}
    return render(request, 'webapp/dashboard.html', context=context)

# - Create a record
@login_required(login_url='my-login')
def create_record(request):
    # # implement this
    # pass
    form = CreateRecordForm()
    
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect("dashboard")
    # to take data to the view
    context = {'form3' : form}
    return render(request, 'webapp/create-record.html', context=context)

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record) # we want to get a particular user record
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect('dashboard')
    context = {'form4':form}
    
    return render(request, 'webapp/update-record.html', context=context)

# Read a record
@login_required(login_url='my-login')
def singular_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}
    return render(request, 'webapp/view-record.html', context=context)

#Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect('dashboard')


# - User Logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "GoodBye < />")
    return redirect("my-login")
