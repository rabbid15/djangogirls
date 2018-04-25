from django.shortcuts import render

# Create your views here.
def payable(request):
	return render(request, 'payable.html',
	{
		'current_time': str(3*5),
	})