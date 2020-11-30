from django.shortcuts import render

def homeView(request):
	context = {}
	return render(request, 'home/home.html', context)