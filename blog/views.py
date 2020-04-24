from django.shortcuts import render

posts = [
    {
        'author': 'Hilde',
        'title': 'blog post 1',
        'content': 'Firstpost hardcoded',
        'date_posted': 'April 23, 2020'
    },
    {
        'author': 'Hildebra',
        'title': 'blog post 2',
        'content': 'Secondpost hardcoded',
        'date_posted': 'April 24, 2020'
    }

]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
