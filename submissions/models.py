from django.db import models
BLOG_TYPES = [
    ('Food', 'Food'),
    ('Travel', 'Travel'),
    ('Business', 'Business'),
    ('Fitness', 'Fitness'),
    ('Fashion', 'Fashion'),
    ('Finance', 'Finance'),
]

class Blog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    blog_type = models.CharField(max_length=50, choices=BLOG_TYPES)
    content = models.TextField()

    def __str__(self):
        return f"{self.blog_type} by {self.name}"

class UserSubmission(models.Model):
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='submissions/', blank=True, null=True)

    def __str__(self):
        return f"{self.location_name} by {self.name}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.name}"
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title    
