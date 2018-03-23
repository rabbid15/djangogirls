from django.shortcuts import render

from datetime import datetime
from django import template


def hello_world(request):
	return render(request, 'hello_world.html',
	{
		'current_time': str(3*5),
	})

def calculate(request):
	result = None
	a=b=c=0
	if request.method == 'POST':
		a = int(request.POST.get('first'))
		b = int(request.POST.get('last'))
		c = str(request.POST.get('operation'))
		return render(request, 'math.html',
		{
			'result':judege(a,b,c)
			
		})
	else:
		return render(request, 'math.html',
		{
			'result':str("test")
		})

def judege(x,y,z):

	switch = {
		'add' : x+y,
		'sub' : x-y,
		'mul' : x*y,
		'div' : x%y
		}
	return switch.get(z,"noting")




# Create your views here.
