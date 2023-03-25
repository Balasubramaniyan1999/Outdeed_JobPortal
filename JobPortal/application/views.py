from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from application.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home(request):
    return render(request,"jobs/index.html")


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Regsitration Success you can login now !")
            return redirect('/login')
    return render(request,'jobs/register.html',{'form':form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username = name,password = pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Loggedin Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password! Try again...")
                return redirect('/login')
        return render(request,"jobs/login.html")
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfully")
    return render(request,'jobs/logout.html')

def jobs(request):
    jobs = Category.objects.filter()
    return render(request,"jobs/collections.html",{'jobs':jobs})

def jobsviews(request,name):
    if(Category.objects.filter(name=name)):
        descriptions = Description.objects.filter(category__name = name)
        return render(request,"jobs/details/index.html",{'description':descriptions,'name':name})
    else:
        messages.error("No Such job categories Not found")
        return redirect('jobs')
    
def job_details(request,cname,dname):
    if(Category.objects.filter(name=cname)):
        if(Description.objects.filter(name=dname)):
            description = Description.objects.filter(name = dname).first()
            return render(request,'jobs/details/job_details.html',{'description':description})
        else:
            messages.error(request,"No such jobs was found")
            return redirect('jobs')
    else:
        messages.error(request,"No such job categories was found")
        return redirect('jobs')