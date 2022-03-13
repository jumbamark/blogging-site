from django import forms
from .models import Post, Category, Comment

# Choices = [("coding", "coding"), ("sports", "sports"), ("politics", "politics")]
Choices = Category.objects.all().values_list("name", "name")

choice_list = []
for item in Choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "title_tag", "snippet",
                  "author", "category", "body", "image"]

        widgets = {
            # creating a widget dict for styling, inside of here we just designate what we want, the title for instance is a text input box,we want to do sth to it - we need to change the attributes of that box: create a class inside of the text input box, pass some css called form-control
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write the title"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control", "id": "author-field", "value": "", "readonly": "True"}),
            "category": forms.Select(choices=choice_list, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write your name"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
