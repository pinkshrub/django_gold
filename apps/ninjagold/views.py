from django.shortcuts import render, redirect
from random import randint
import datetime

# Create your views here.
def index(request):
	try:
		request.session['gold_earned']
	except:
		request.session['gold_earned'] = 0
	context = {}
	return render(request, 'ninjagold/index.html', context)

def bank(request):
	act = request.POST['action']
	earnings = {
		'cave': (randint(0,10)),
		'house': 4,
		'farm': (randint(3,6)),
		'dragon':  (randint(-50,50)),
	}
	print '-9-'*10
	print earnings[act]
	request.session['gold_earned'] += earnings[act]
	time = datetime.date.today()
	try:
		request.session['log']
	except:
		request.session['log']=[]
	request.session['log'].append('ninja went to the '+ str(act) + 'and profitted: '+ str(earnings[act]) + ' on ' + str(time))


	return redirect('/')