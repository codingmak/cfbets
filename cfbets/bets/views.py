import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from bets.forms import PlaceBetsForm

# Create your views here.

def bets(request):
	return HttpResponseRedirect('/bets/my_bets');

@login_required(login_url='/login/')
def my_bets(request):
	return render(request, 'bets/base_my_bets.html', {'nbar': 'my_bets'})

@login_required(login_url='/login/')
def open_bets(request):
	return render(request, 'bets/base_open_bets.html', {'nbar': 'open_bets'})

@login_required(login_url='/login/')
def all_bets(request):
	return render(request, 'bets/base_all_bets.html', {'nbar': 'all_bets'})

def place_bets_form_process(request, next_url):
	if request.method == 'POST':
        	form = PlaceBetsForm(request.POST)
		if form.is_valid():
			# do something with this form eventually
			response = {'url': next_url}
			messages.success(request, 'Bet submitted succesfully (to nothing until I get that data model).')
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			# form isn't valid, return to ajax call with error and form with errors
			return render(request, 'bets/place_bets.html', {'place_bets_form': form}, status=400)

	return HttpResponseRedirect('/bets/my_bets')
	

@staff_member_required(login_url='/')
def admin_bets(request):
	return render(request, 'bets/base_admin_bets.html', {'nbar': 'admin_bets'})
