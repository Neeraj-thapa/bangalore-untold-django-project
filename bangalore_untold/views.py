from django.shortcuts import render, redirect
from .models import Blog, Feedback
from .forms import BlogForm, FeedbackForm

# Home Page
def home(request):
    return render(request, 'main/home.html')

# Blog Page
def blog(request):
    blogs = Blog.objects.order_by('?')[:10]  # Show random blogs
    return render(request, 'main/blog.html', {'blogs': blogs})

# Submit Blog
def submit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirect back to Blog Page
    else:
        form = BlogForm()
    return render(request, 'main/submit_blog.html', {'form': form})

# FAQ Page
def faq(request):
    return render(request, 'main/faq.html')

# Submit Feedback
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')  # Redirect back to FAQ Page
    else:
        form = FeedbackForm()
    return render(request, 'main/faq.html', {'form': form})
