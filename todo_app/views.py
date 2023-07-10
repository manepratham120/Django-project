from django.shortcuts import render,redirect
from todo_app.models import tasklists
from todo_app.forms import taskform
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from .forms import CustomRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
    if request.method=="POST":
        form=taskform(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request, ("New task added !"))    
        return redirect('todolist')    
    else:
      all_task=tasklists.objects.filter(manage=request.user)
      paginator=Paginator(all_task,5)
      page=request.GET.get('pg')
      all_task=paginator.get_page(page)
      
      return render(request , 'index.html',{'all_task':all_task} )

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task=tasklists.objects.get(pk=task_id)
        form=taskform(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        
        messages.success(request, (" task edited !"))    
        return redirect('todolist')    
    else:
      task_obj=tasklists.objects.get(pk=task_id) 
      return render(request , 'edit.html',{'task_obj':task_obj})

@login_required    
def delete_task(request, task_id):
    task=tasklists.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task=tasklists.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task=tasklists.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login To Get Started!"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})    
                
            
def about(request):
    return render(request , 'about.html', {})

def contact(request):
    return render(request , 'contact.html', {})

def home(request):
    return render(request , 'home.html', {})



def pending(request):
    return render(request , 'pending.html', {})