from django.shortcuts import render,redirect
import random

def index(request):
	if "gold" not in request.session:
		request.session['gold'] = 0
	return render(request,"main/index.html")

def process(request):
	stat = "stat"
	zero = 0;
	farm = random.randrange(10,20);
	cave = random.randrange(5,10);
	house = random.randrange(2,5);
	casino = random.randrange(-50,50);

	if request.POST.get('farmgold'):
		request.session['gold'] += farm
		request.session['win'] = "you have won {} gold!".format(farm)
		request.session['lost'] = ""
		request.session['luck'] =""
		return redirect('/')
	
	elif request.POST.get('cavegold'):
		request.session['gold'] += cave
		request.session['win'] = "you have won {} gold!".format(cave)
		request.session['lost'] = ""
		request.session['luck'] =""
		return redirect('/')
	
	elif request.POST.get('housegold'):
		request.session['gold'] += house
		request.session['win'] = "you have won {} gold!".format(house)
		request.session['lost'] = ""
		request.session['luck'] =""
		return redirect('/')
	
	elif request.POST.get('casinogold'):
		request.session['gold'] += casino
		if casino > 0:
			request.session['win'] = "you have won {} gold!".format(casino)
			request.session['lost'] = ""
			request.session['luck'] =""
		elif casino < 0:
			request.session['win'] = ""
			request.session['lost'] = "you have Lost {} gold!".format(casino)
			request.session['luck'] =""
		return redirect('/')


	elif request.POST.get('reset'):	
			request.session['gold'] = 0
			request.session['win'] =""
			request.session['lost'] =""
			request.session['max'] = 0
			request.session['min']= 0
			request.session.clear()
			request.session['luck'] ="Good Luck!"

			return redirect('/')
# Create your views here.
