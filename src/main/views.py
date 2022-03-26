from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Contact

# index view function
def index_page(request):
#  return HttpResponse("Hello, world. ")
   return render(request, 'main/index.html')

# about view function
def about_page(request):
   return render(request, 'main/about.html')

# signup view function
def signup_page(request):
   if request.method == 'POST':
      fm = SignUpForm (request.POST)
      if fm.is_valid():
         messages.success(request, 'Account Created Successfully!!')
         fm.save()            
   else:
      fm = SignUpForm ()

   return render(request, 'main/signup.html', {'form':fm})

# login view function
def login_page(request):
   if request.method == 'POST':
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():            
         uname = fm.cleaned_data['username']
         upass = fm.cleaned_data['password']
         user = authenticate( username=uname, password=upass)
         if user is not None:
            login(request, user)            
         return HttpResponseRedirect('/profile/')
   else:
      fm = AuthenticationForm()    
   return render(request, 'main/login.html', {'form':fm})

# logout view function
def logout_page(request):   
   return render(request, 'main/logout.html')

# profile view function
def profile_page(request):
   messages.success(request, 'You have logged in successfully!!')  
   return render(request, 'main/profile.html', {'name':request.user})

# contact view function
def contact_page(request):
   thank = False
   if request.method == "POST":
      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      phone = request.POST.get('phone', '')
      message = request.POST.get('message', '')
      contact = Contact(name=name, email=email, phone=phone, message=message)
      messages.success(request, 'Message sent Successfully!!')
      contact.save()
      thank = True
   return render(request, 'main/contact.html', {'thank': thank})
