from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import json
from django.contrib import auth
from . import models
from .models import UserInfo, Recipe
from django.contrib.auth.models import User
# Create your views here.

def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {"recipes": recipes})
    
def sign_in(request):
    if request.method == "GET":
        return render(request, "sign_in.html")
    elif request.method == "POST":
        userid = request.POST["userid"]
        password = request.POST["pw"]
        user = auth.authenticate(request, username = userid, password = password)
        if user is None:
            return render(request, "sign_in.html")
        auth.login(request, user)
    return redirect('main:main')

def sign_out(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('main:main')


def sign_up(request):
    if request.method == "GET":
        return render(request, "sign_up.html")
    elif request.method == "POST":
        user = UserInfo()
        user.username = request.POST.get("username", True)
        user.userid = request.POST["userid"]
        user.user_birth_year = request.POST.get("user_birth_year", True)
        user.user_birth_month = request.POST.get("user_birth_month", True)
        user.user_birth_day = request.POST.get("user_birth_day",True)
        user.password = request.POST.get("pw",True)
        user.password_check = request.POST.get("pw_check",True)
        user.phonenumber = request.POST.get("phonenumber",True)
        user.address = request.POST.get("address",True)
         
        if User.objects.filter(username = request.POST.get('username')):
            return HttpResponse('아이디가 중복입니다.')
        if user.password != user.password_check:
            return render(request, "sign_up.html")
        user.save()
    return redirect('main:main')

def sign_search(request):
    return render(request, 'sign_search.html')

def sign_search_id_page(request):
    return render(request,"sign_search_id.html")

def sign_search_id(request):
    phonenumber = request.GET.get("phonenumber")
    user = UserInfo.objects.filter(phonenumber = phonenumber)
    content = user[0].userid
    context = {"content":content}
    return HttpResponse(json.dumps(context),content_type="application/json")

def sign_search_password_page(request):
    return render(request,"sign_search_password.html")

def sign_search_password(request):
    userid = request.GET.get("userid")
    user = UserInfo.objects.filter(userid = userid)
    content = user[0].password
    context = {"content":content}
    return HttpResponse(json.dumps(context),content_type="application/json")

def search(request):
    valid_recipes = Recipe.objects.filter(recipe_name__contains = request.GET['recipe_name'])

    return render(request, "main.html", {'recipes': valid_recipes})

