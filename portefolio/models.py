from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, SlugField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField

from account.models import Profile
from blog.models import Tag

# Create your models here.


class Project(models.Model):
    profile = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    title = CharField(max_length=120)
    slug = SlugField(max_length=120)
    description = TextField(null=True, blank=True)
    image = ImageField(null=True, blank=True, upload_to="projects/")
    source_link = CharField(max_length=200, blank=True)
    demo_link = CharField(max_length=200, blank=True)
    vote = IntegerField(default=1)

    state = BooleanField(default=False, choices=(
        (True, "Activate"), (False, "Deactivated")))
    tags = ManyToManyField(Tag)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
