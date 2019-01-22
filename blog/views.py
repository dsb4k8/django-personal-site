from django.shortcuts import render
#from django.http import HttpResponse

posts = [
{
	'author': 'DiegoSB',
	'title': 'Blog Post 1',
	'content': 'First post content',
	'date_posted':'January 22, 2019'
},
{
	'author': 'SomeoneEE',
	'title': 'Blog Post 2',
	'content': 'Second post content',
	'date_posted':'January 22, 2019'
},
{
	'author': 'ThirdisonTD',
	'title': 'Blog Post 3',
	'content': 'Third post content',
	'date_posted': 'January, 23, 2019'
},
]


def home(request):
	context = {
		'posts': posts
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
