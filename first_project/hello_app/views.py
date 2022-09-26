from django.shortcuts import render 
from django.http import HttpResponse

def index(request):

	my = {"show_me": "Hello I am from index.html! "}
	return render(request, 'hello_app/index.html', context=my)
	# return HttpResponse('<h1>Hello world </h1>')