from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Admin")
    content = HTMLField()
    cover_image = models.ImageField(upload_to='blog_covers/', default='default_cover.jpg',null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)  # Name of the commenter
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"


class PracticeArea(models.Model):
    name = models.CharField(max_length=100, verbose_name="Area of Practice")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g., 'fa-scale-balanced'")
    detailed_description = HTMLField(verbose_name="Detailed Description")
    slug = models.SlugField(unique=True, help_text="URL-friendly name for the practice area")

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name   