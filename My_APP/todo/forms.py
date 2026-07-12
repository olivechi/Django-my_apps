from django import forms
from .models import BlogPost, Contact


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Post title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Write your blog content here"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "What is this about?"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Tell me more..."}),
        }
