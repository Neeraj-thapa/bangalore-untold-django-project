from django import forms
from .models import Blog, UserSubmission, Feedback

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
