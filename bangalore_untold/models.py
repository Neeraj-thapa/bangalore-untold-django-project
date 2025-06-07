from django.db import models

# Blog Model
class Blog(models.Model):
    BLOG_CATEGORIES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Business', 'Business'),
        ('Fitness', 'Fitness'),
        ('Fashion', 'Fashion'),
        ('Finance', 'Finance'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=BLOG_CATEGORIES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.name}"

# Feedback Model
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
