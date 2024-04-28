from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, add_employee, update_employee

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Employee

def home(request):
    
    return render(request, 'webapp/index.html')



# register view

def register(request):
    form = CreateUserForm() # Inheriting from the CreateUserForm clas

    if request.method =='POST': # Making a post request from the register.html. Essentially,
        # it is sending data to the database.
        form = CreateUserForm(request.POST) # Posting the request data

        if form.is_valid():
            form.save() # Posting the data or saving it

            messages.success(request, 'Account created successfully')
            return redirect('my_login')
    
    context = {'form':form}

    return render(request, 'webapp/register.html',context=context)


# login a user

def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            passw = request.POST.get('password')

            user = authenticate(request, username=username, password=passw)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')


    context = {'login_form':form}
    return render(request, 'webapp/my_login.html', context=context)


# User logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Logout success!')

    return redirect('my_login')


# User dashboard
@login_required(login_url='my_login')
def dashboard(request):

    my_records = Employee.objects.all()
    context = {'records':my_records}
    return render(request, 'webapp/dashboard.html', context=context)


# Adding an employee
@login_required(login_url='my_login')
def create_employee(request):
    form = add_employee()
    if request.method == 'POST':
        form = add_employee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details was added successfully!')

            return redirect('dashboard')
        
    context = {'addemployee': form}

    return render(request, 'webapp/create_record.html', context=context)

# Updating an employee
@login_required(login_url='my_login')
def edit_employee(request, pk):
    record = Employee.objects.get(id=pk)
    form = update_employee(instance=record) # Taking the kind of employee id we want to edit and passing it to the Update_employee form

    if request.method == 'POST':
        form = update_employee(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your employee details was updated')
            return redirect('dashboard')
        
    context = {'editemployee':form}

    return render(request, 'webapp/update_record.html', context=context)

# View an employee
@login_required(login_url='my_login')
def view_employee(request, pk):
    all_records = Employee.objects.get(id=pk)
    context = {'employee':all_records}

    return render(request, 'webapp/view_record.html', context=context)

# Delete an employee
@login_required(login_url='my_login')
def delete_record(request, pk):
    record = Employee.objects.get(id=pk)

    record.delete()
    messages.success(request, 'Your employee details was deleted')

    return redirect("dashboard")