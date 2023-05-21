from django.shortcuts import render

from .models import Post, Category


# Create your views here.
def home(request):
    post = Post.objects.all()
    cat = Category.objects.all()
    return render(request, 'brity/index.html' ,{'post': post , 'cat': cat})

def details_post(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'brity/details_post.html',{'post': post})
def details_category(request, category_id):
    cat = Category.objects.get(id=category_id)
    return render(request, 'brity/category.html',{'cat': cat})

