from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("skills/", views.skills_page, name="skills"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/create/", views.blog_create, name="blog_create"),
    path("blog/<int:pk>/edit/", views.blog_update, name="blog_update"),
    path("blog/<int:pk>/delete/", views.blog_delete, name="blog_delete"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
