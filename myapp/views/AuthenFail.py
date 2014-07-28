from django.shortcuts import render

def index(request):
	ex = request.GET["ex"]
	context={"ex":ex}
	return render(request, 'myapp/error-page.html', context)