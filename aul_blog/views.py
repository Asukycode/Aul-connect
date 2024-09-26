from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import blog_post
# Create your views here.

def blog_home(request):
    blog_posts = blog_post.objects.all()
    context = {
        "blog_posts": blog_posts
    }
    return render(request, 'aul_blog/blog.html', context)

def blog_create(request):
    if request.method == 'POST' and request.FILES['image']:
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        tags = request.POST.get('tags')
        category = request.POST.get('category')

        if title and content and image and tags and category:
            blog_post.objects.create(
                title=title,
                content=content,
                image=image,
                tags=tags,
                category=category
            )
            return redirect('blog_post_success')
        else:
            error_message = "Please fill in all required fields."
            return render(request, 'aul_blog/blog_post_create.html', {'error_message': error_message})
    return render(request, 'aul_blog/blog_post_create.html')

def blog_detail(request, id=None):
    if id is not None:
        post = blog_post.objects.get(id=id)
        context = {
            "blog_post": post, 
        }
    return render(request, 'aul_blog/blog_detail.html', context=context)
def blog_post_success(request):
    return render(request, 'aul_blog/blog_post_create_success.html')