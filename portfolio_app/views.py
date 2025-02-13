from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Project, Experience, BlogPost

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send email directly to email
        send_mail(
            f"Message from {name} ({email})",  # Subject
            message,  # Message body
            email,  # From this email 
            ['muthokasam001@gmail.com'],
        )
        
        # Optionally, you can display a success message here
        return render(request, 'portfolio_app/home.html', {'message_sent': True})
    
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects, 'experiences': experiences})

def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    blog_posts = BlogPost.objects.all().order_by('-created_at')  # Fetch and order blog posts by latest
    return render(request, 'portfolio_app/home.html', {
        'projects': projects,
        'experiences': experiences,
        'blog_posts': blog_posts
    })
    
def blog_detail(request, id):
    post = BlogPost.objects.get(id=id)
    return render(request, 'portfolio_app/blog_detail.html', {'post': post})

def blog_post(request):
    return render(request, 'portfolio/blog_post.html')
