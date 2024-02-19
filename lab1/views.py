from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from lab1.models import Student

# Create your views here.
def home(request):
    return render (request ,'lab1/home.html')

def viewstd(request):
    students = Student.objects.all()
    context = {}
    context['students'] = students
    return render (request ,'lab1/viewstd.html',context)

def deletestd(request,id):
    Student.objects.get(id=id).delete()
    return redirect (viewstd)
    
def signup(request):
    if request.method == 'GET':
        return render(request,'lab1/signup.html')
    
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        data=Student.objects.filter(username=username,password=password)
        
        if data:
            return render(request,'lab1/signup.html')
        
        Student.objects.create(email=email, password=password, username=username)
        return redirect("signin")
        
def signin(request):
    if request.method == 'GET':
        return render(request,'lab1/signin.html')
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        data=Student.objects.filter(username=username,password=password)
        
        if data:
            return redirect("home")
        else:
            return render(request,'lab1/signin.html')    
