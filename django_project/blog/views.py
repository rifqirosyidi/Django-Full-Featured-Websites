from django.shortcuts import render

# Create your views here.

dummy_posts = [
    {
        'author': 'Rifqi Rosyidi',
        'title': 'Posted 1',
        'content': 'Content Of Posted One By Rief',
        'date_posted': '21 August, 2019',
    },
    {
        'author': 'Neuron Planets',
        'title': 'Posted 2',
        'content': 'Content Of Posted Two By Neuron Planets',
        'date_posted': '24 August, 2019',
    },
]


def home(request):
    context = {
        'posts': dummy_posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
