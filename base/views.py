from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Blog, Comment, PracticeArea, TeamMember
from .forms import CommentForm



def home(request):
    blogs = Blog.objects.order_by('-published_at')[:4]
    practice_areas = PracticeArea.objects.all()
    
    context={'practice_areas': practice_areas,
             'blogs': blogs, 'MEDIA_URL': settings.MEDIA_URL
            }
    return render(request, 'base/home.html',context)

def about_us(request):
    return render(request, 'base/about.html')

 
def team_page(request):
    team_members = TeamMember.objects.all()
    practice_areas = PracticeArea.objects.all
    
    context={
        'team_members': team_members,'practice_areas': practice_areas,
    }
    return render(request, 'base/team.html',context)

    

def blog(request, blog_id=None):
    blogs = Blog.objects.order_by('-published_at')  # List blogs, latest first
    active_blog = blogs.first() if not blog_id else get_object_or_404(Blog, id=blog_id)
    practice_areas = PracticeArea.objects.all
    
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        if name and text:
            Comment.objects.create(blog=active_blog, name=name, text=text)
            return redirect('blog_page', blog_id=active_blog.id)

    return render(request, "base/blog.html", {
        "active_blog": active_blog,
        "blogs": blogs, 'MEDIA_URL': settings.MEDIA_URL,
        'practice_areas': practice_areas,
    })


def practice_area_detail(request, slug):
    practice_area = get_object_or_404(PracticeArea, slug=slug)
    practice_areas = PracticeArea.objects.all()
    return render(request, 'base/practice.html', {'practice_area': practice_area, 'practice_areas': practice_areas,})


