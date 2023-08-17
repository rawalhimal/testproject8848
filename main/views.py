from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
# Create your views here.
from .models import BlogCategory,BlogPost
def home(request):
    if request.user.is_authenticated:
        categorires = BlogCategory.objects.all()
        fnews = BlogPost.objects.all()
        context = {
            'categorires':categorires,
            'fnews':fnews,
        }
        return render(request,'index.html',context)
    else:
        return redirect('login_form')

def send_email(request):
    if request.method == 'POST':
        print("code ---")
        email = request.POST['email']
        print(email)
        subject = 'Python Training at Sipalaya'
                #  message = 'This is a test email from Django!'
        message = render_to_string('test.html')
        from_email = 'himalrawal500@gmail.com'
        recipient_list = ['premoli371@gmail.com',email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False,html_message=message)
    return HttpResponse("Successfull !!")


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_form')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})
# sipalaya , Password123@
def login_form(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_form')
    
    return render(request,'login.html')

def logout_form(request):
    logout(request)
    return redirect('login_form')