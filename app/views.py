from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, Employer
# Create your views here.
def home(request):
  if request.method == 'POST':
     username =request.POST.get('username')
     email =request.POST.get('email')
     password =request.POST.get('password')
     confirm_password =request.POST.get('confirm_password')
   
     if password != confirm_password:
         messages.error(request, 'Password do not match')
         return redirect('home')
     elif User.objects.filter(username=username).exists():
          messages.error(request, 'Username already exists')
          return redirect('home')
     elif User.objects.filter(email=email).exists():
          messages.error(request, 'Email already exists')
          return redirect('home')

     else:
          user= User.objects.create_user(username=username,email=email,password=password)
          user.save()
          messages.success(request, 'User created successfully')
          return redirect('home')
  return render(request,'home.html')

def contact(request):
     if request.method == 'POST':
          full_name = request.POST.get('full_name')
          email = request.POST.get('email')
          subject =request.POST.get('subject')
          message =request.POST.get('message') 

          contact = Contact(full_name=full_name,email=email,subject=subject,message=message)
          contact.save()
          messages.success(request, 'Your message has been sent successfully!')
          return redirect('contact')
          
     return render(request,'contact.html')

def employer(request):
     if request.method == 'POST':
         full_name=request.POST.get('full_name')
         email=request.POST.get('email')
         employer_id=request.POST.get('employer_id')
         date_hired=request.POST.get('date_hired')
         department=request.POST.get('department')
         
         emp = Employer(
             full_name=full_name,
             email=email,
             employer_id=employer_id,
             date_hired=date_hired,
             department=department,
         )
         emp.save()
         messages.success(request, 'Employer successfully registered')
         return redirect('employer')
     return render(request,'employer.html')