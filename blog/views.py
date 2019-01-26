from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

def home(request):
	context = {
		'posts': Post.objects.all()
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def projects(request):
	return render(request, 'blog/projects', {'title': 'Projects'})

# def hue(request):
# 	return render(rewuest, 'blog/')
