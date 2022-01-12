from django.forms import *
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = "__all__"
        # fields = ['title', 'description', 'category', 'tags']
        exclude = ['state']
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
            "category": Select(attrs={"class": "form-control"}),
            "tags": SelectMultiple(attrs={"class": "form-control"})


        }
