from django.shortcuts import render,redirect
from .models import *
import bcrypt
def index(request):

	return render(request,"main/index.html")
def success(request):
	return render(request,"main/success.html")	

def sessions(request):
	login = User.objects.sessions(request.POST)
	print login
	if login:
		request.session['user_id'] = login[1].id
		return redirect('/success')
	return redirect('/')		


def create_user(request):
	if User.objects.validate_user(request.POST):
		user = User.objects.create(
			first_name = request.POST.get('first_name'),
			last_name = request.POST.get('last_name'),
			email = request.POST.get('email'),
			password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
		)
		request.session['user_id'] = user.id
		return redirect('/success')
	return redirect('/')	




# Create your views here.
