from django.shortcuts import render,redirect
from models import *
from django.contrib import messages
import re
import datetime
import bcrypt
DATE_REGEX =  re.compile(r'^(19|20)\d\d[\-\/.](0[1-9]|1[012])[\-\/.](0[1-9]|[12][0-9]|3[01])$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
	return render(request,"main/index.html")


def register(request):
	if len(request.POST.get('name'))<3:
		messages.warning(request,"Name is not valid")
		return redirect('/')
	elif len(request.POST.get('username'))<3:
		messages.warning(request,"Email is invalid")
		return redirect('/')
	elif EMAIL_REGEX.match(request.POST.get('hired')):
		messages.warning(request,"Date Hired is invalid")	
		return redirect('/')
	elif len(request.POST.get('password'))<6:
		messages.warning(request, "Password must be atleast 6 charachters in length")
		return redirect('/')
	elif request.POST.get('password') != request.POST.get('confirm'):
		messages.warning(request,"Passwords do not match")
		return redirect('/')
	else:
		user = User.objects.create(name=request.POST.get('name'),Username=request.POST.get('username'),password=bcrypt.hashpw(request.POST.get('password').encode(),bcrypt.gensalt()),hired=request.POST.get('hired'))
		request.session['user_id']=user.id
		return redirect('/dashboard')	
def dashboard(request):
	context = {
		'list': List.objects.filter(user__id=request.session['user_id']),
		'other': List.objects.exclude(user__id=request.session['user_id']),
	}
	return render(request,"main/dashboard.html", context)
def remove(request,id):
	List.objects.filter(id=id).delete()
	return redirect('/dashboard')
def plus(request):
	# listList.objects.create(item=request.POST.get('item'),user = User.objects.get(id=request.session['user_id'])),
	return redirect('/dashboard')		
def postit(request):
	if len(request.POST.get('item'))<3:
		messages.warning(request,"Item name is too short")
		return redirect('/add')
	else:
		items = List.objects.create(item=request.POST.get('item'),user = User.objects.get(id=request.session['user_id'])),
		
	return redirect('/dashboard')	
def show(request,id):
	context = {
		'show': List.objects.filter(id=id),
	}
	return render(request, "main/show_item.html",context)
def logout(request):
	request.session.clear()
	return redirect('/')	
def add(request):
	return render(request,"main/add.html")	

def login(request):
	login = User.objects.login(request.POST)
	if login[0]:
		request.session['user_id']=login[1].id
		return redirect('/dashboard')
	else:
		messages.warning(request,'User does not exsist')
		return redirect('/')				