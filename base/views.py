from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .models import Blog, Comment, PracticeArea, TeamMember, Job
from .forms import CommentForm, ContactForm


def base_context(request):
    return {
        'first_practice_area': PracticeArea.objects.first()
    }
def home(request):
    blogs = Blog.objects.order_by('-published_at')[:4]
    practice_areas = PracticeArea.objects.all()
    form = ContactForm()  # Default empty form
    success_message = None  # Variable to hold success message

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send email
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(subject, body, email, ["oswereenock@gmail.com"])

            success_message = "Your message has been sent successfully!"

            # Reset the form after successful submission
            form = ContactForm()

    context = {
        'practice_areas': practice_areas,
        'first_practice_area': PracticeArea.objects.first(),
        'blogs': blogs,
        'form': form,  # ✅ Ensure the form is passed to the template
        'success_message': success_message,  # ✅ Ensure success message is passed
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'base/home.html', context)
def about_us(request):
    practice_areas = PracticeArea.objects.all
    context={
        'practice_areas': practice_areas,
    }
    return render(request, 'base/about.html',context)

 
def team_page(request):
    team_members = TeamMember.objects.all()
    practice_areas = PracticeArea.objects.all
    
    context={
        'team_members': team_members,'practice_areas': practice_areas,
    }
    return render(request, 'base/team.html',context)

    

def blog(request, blog_id=None):
    practice_areas = PracticeArea.objects.all
    blogs = Blog.objects.order_by('-published_at')
    active_blog = blogs.first() if not blog_id else get_object_or_404(Blog, id=blog_id)
    comments = active_blog.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = active_blog
            comment.save()
            return redirect('blog_page', blog_id=active_blog.id)
    else:
        form = CommentForm()

    return render(request, "base/blog.html", {
        "active_blog": active_blog,
        "blogs": blogs,'practice_areas': practice_areas,
        "comments": comments,  # ✅ Pass comments (with admin responses)
        "form": form,
    })
def practice_areas_main(request):
    practice_areas = PracticeArea.objects.all()
    return render(request, 'base/practice.html', {'practice_areas': practice_areas})

def practice_area_detail(request, slug):
    practice_area = get_object_or_404(PracticeArea, slug=slug)
    practice_areas = PracticeArea.objects.all()
    return render(request, 'base/practice.html', {'practice_area': practice_area, 'practice_areas': practice_areas,'first_practice_area': PracticeArea.objects.first()})

def careers(request):
    jobs = Job.objects.all()
    return render(request, 'base/careers.html', {'jobs': jobs})




