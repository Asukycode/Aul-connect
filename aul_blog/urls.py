from django.urls import path
from .views import blog_home, blog_create, blog_detail, blog_post_success

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('blog_create/', blog_create, name='blog_create'),
    path("blog_post/<int:id>", blog_detail , name="blog_detail"),
    path('success/', blog_post_success, name='blog_post_success'),
    # Add more paths here
]