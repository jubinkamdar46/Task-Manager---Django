from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from manageusers.models import Users,Tasks

# to display duplicate entry problem
from django.db import IntegrityError

# to show alert messages 
from django.contrib import messages


# Create your views here.

def register(request):
     # fetching data from register form

    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            address = request.POST['address']
            age = request.POST['age']
            occupation = request.POST['occupation']
            state = request.POST['state']
            city = request.POST['city']
            gender = request.POST['optradio']
            zipcode = request.POST['zipcode']

            user = Users(user_email=email,user_password=password,user_age=age,user_occupation=occupation,user_gender=gender,user_state=state,user_zipcode=zipcode)
            user.save()
            messages.success(request, 'Thank You For Registering.')
            return render(request,"login.html")     
        except IntegrityError:
            messages.warning(request, 'Email is already taken.')

    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_data = Users.objects.filter(user_email=email,user_password=password).exists()
        if(user_data):
            user_info = Users.objects.filter(user_email=email).values()
            session_email = request.session["email"] = email
            return redirect("home")
        else:
            messages.warning(request, 'No Account Found')
    return render(request,'login.html')

def home(request):
    task_data = Tasks.objects.all()
    recent_task = Tasks.objects.last()
    return render(request,"home.html",{"task_data":task_data,"recent_task":recent_task})

def addTask(request):
    if request.method == "POST":
        task_name = request.POST.get("taskname")
        task_decs = request.POST.get("taskdecription")
        task_due = request.POST.get("duedate")
        task_priority = request.POST.get("priority")
        task_assignto = request.POST.get("assignto")
        task_assignee = request.session.get('email')
        print(task_assignee)
        print(task_due)
        task = Tasks(task_title=task_name,task_description=task_decs,task_duedate=task_due,task_priority=task_priority,task_assignee=task_assignee,task_assignto=task_assignto)
        task.save()
        return redirect("home")
    else:
        user_data = Users.objects.all
        print(user_data)
        return render(request,"add_task.html",{"user_emails":user_data})

def deleteTask(request,taskid):
    Tasks.objects.filter(id = taskid).delete()
    return redirect("home")

def updateTask(request,taskid):
    if request.method == "POST":
        t = Tasks.objects.get(id=taskid)
        t.task_title = request.POST.get("taskname")
        t.task_description = request.POST.get("taskdecription")
        t.task_duedate = request.POST.get("duedate")
        t.save()
        return redirect("home")
    else:
        task = Tasks.objects.filter(id = taskid)
        return render(request,"updatetask.html",{"task_details":task})

def logout(request):
    del request.session["email"]
    return redirect("welcome")