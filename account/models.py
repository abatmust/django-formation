from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, EmailField, TextField, UUIDField
from django.db.models.fields.files import ImageField
from uuid import uuid4

from django.contrib.auth.models import User


from django.db.models.fields.related import OneToOneField
# Create your models here.


class Profile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=80)
    username = CharField(max_length=80, unique=True, null=True, blank=True)
    email = EmailField(max_length=120, null=True, blank=True, unique=True)
    head_line = CharField(max_length=200, null=True, blank=True)
    bio = TextField(null=True, blank=True)
    image = ImageField(null=True, blank=True,
                       upload_to="profiles/", default="profiles/default.png")
    resume_link = CharField(max_length=200, null=True, blank=True)
    github_link = CharField(max_length=200, null=True, blank=True)
    linkdin_link = CharField(max_length=200, null=True, blank=True)
    youtube_link = CharField(max_length=200, null=True, blank=True)
    website_link = CharField(max_length=200, null=True, blank=True)

    state = BooleanField(default=False, choices=(
        (True, "Activate"), (False, "Deactivated")))
    id = UUIDField(primary_key=True, unique=True,
                   default=uuid4,  editable=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
