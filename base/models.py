from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Admin")
    content = RichTextField()
    cover_image = models.ImageField(upload_to='blog_covers/', default='default_cover.jpg',null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin_response = models.TextField(blank=True, null=True)  # ✅ New Field

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"


class PracticeArea(models.Model):
    name = models.CharField(max_length=100, verbose_name="Area of Practice")
    image = models.ImageField(upload_to="practice_areas/", help_text="Upload an image representing the practice area",null=True, blank=True)

    detailed_description = RichTextField(verbose_name="Detailed Description")
    slug = models.SlugField(unique=True, help_text="URL-friendly name for the practice area")

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name 
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title  