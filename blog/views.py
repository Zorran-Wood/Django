from django.shortcuts import render
from .models import Post#the . in .models is accessed because its in the same directory or project and we can import it via a dotnotation like style

# Create your views here.
#def is how you declare a method


posts = [

    {

        'author': 'ZOLTAN-OPS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Ausgust 29, 2021'
    }

]




def home(request):#when this is accessed by blog.urls it sends back this HttpResponse

    context = {

    'posts': Post.objects.all()#grabs all posts from data base

    }

    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title' : 'big boobs'})


def cyclura(request):
    return render(request, 'blog/cyclura.html', {'title' : 'cyclura'})







