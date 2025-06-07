from django.shortcuts import render, redirect
from .forms import BlogForm, UserSubmissionForm, FeedbackForm
from .models import Blog

def landing(request):
    return render(request, 'submissions/landing.html')

def home(request):
    return render(request, 'home.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'submissions/blog.html', {'blogs': blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'submissions/add_blog.html', {'form': form})

def user_submissions(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserSubmissionForm()
    return render(request, 'submissions/user_submissions.html', {'form': form})

def faq(request):
    return render(request, 'submissions/faq.html')

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')
    return redirect('faq')


from django.shortcuts import render
from .models import Event, Blog

def event_list(request):
    events = Event.objects.all()
    return render(request, 'submissions/events.html', {'events': events})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'submissions/blog.html', {'blogs': blogs})



def map_view(request):
    return render(request, 'submissions/map.html')

def nature(request):
    return render(request, 'explore/nature.html')

def markets(request):
    return render(request, 'explore/markets.html')

def historic(request):
    return render(request, 'explore/historic.html')

def cafes(request):
    return render(request, 'explore/cafes.html')
def explore(request):
    return render(request, 'explore.html')  # adjust the filename if needed

