from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        request.session['name'] = fname
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=fname, last_name=lname, email=email, password=pw_hash)
        return redirect("/wall")

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
        request.session['name'] = user[0].first_name
        return redirect("/wall")
    else:
        return redirect("/")

def wall(request):
    context = {
        "messages": Messages.objects.all(),
        "comments": Comments.objects.all(),
        "currentuser": request.session['name'],
    }
    return render(request, "wall.html", context)

def logout(request):
    request.session['name'] = ""
    return redirect("/")

def message(request):
    message = request.POST['message']
    user = User.objects.get(first_name=request.session['name'])
    request.session['message'] = message
    Messages.objects.create(message=message, user=user)
    return redirect("/wall")

def comment(request, message_id):
    comment = request.POST['comment']
    message = Messages.objects.get(id=message_id)
    user = User.objects.get(first_name=request.session['name'])
    Comments.objects.create(comment=comment, message=message, user=user)
    return redirect("/wall")