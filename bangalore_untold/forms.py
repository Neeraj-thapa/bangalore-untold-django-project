from django import forms
from .models import Blog, Feedback

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'email', 'category', 'content']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
