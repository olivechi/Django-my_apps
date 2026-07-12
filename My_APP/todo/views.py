from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogPostForm, ContactForm
from .models import BlogPost, Contact, Skill


def home(request):
    skills = Skill.objects.all()[:4]
    posts = BlogPost.objects.all()[:3]
    return render(request, "home.html", {"skills": skills, "posts": posts})


def skills_page(request):
    skills = Skill.objects.all().order_by("name")
    return render(request, "skills.html", {"skills": skills})


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, "blog_list.html", {"posts": posts})


def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your blog post has been created.")
            return redirect("blog_list")
    else:
        form = BlogPostForm()
    return render(request, "blog_form.html", {"form": form, "title": "Create Blog Post"})


def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your blog post has been updated.")
            return redirect("blog_list")
    else:
        form = BlogPostForm(instance=post)
    return render(request, "blog_form.html", {"form": form, "title": "Update Blog Post"})


def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "The blog post was removed.")
        return redirect("blog_list")
    return render(request, "blog_delete_confirm.html", {"post": post})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out. Your message has been saved.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def about(request):
    return render(request, "about.html", {"name": "Olive Chimeziri"})


