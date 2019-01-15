from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse

# posts = [
#     {
#         'author':'coreyMS',
#         'title' : 'blog post 1 ',
#         'content' : 'first post content',
#         'date_posted':'Aug 27 , 2018'

#     },
#     {
#         'author':'Jane Doe',
#         'title' : 'blog post 2 ',
#         'content' : 'second post content',
#         'date_posted':'Aug 28 , 2018'

#     }
# ]


@login_required
def home(request):
    context = {
        'posts'  : Post.objects.all() ,
        'title'  : 'Home' 
    }
    return render(request , 'blog/home.html' , context )

@login_required
def about(request):
    return render(request , 'blog/about.html' , { 'title' : 'About' })























