from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, SlugField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.text import slugify
from django.urls import reverse
from account.models import Profile
LIST_STATE = (
    (0, "disable"),
    (1, "enable")
)

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = "categorie"

    name = CharField(max_length=20)
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):

    name = CharField(max_length=20)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    profile = ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    state = IntegerField(default=0, choices=LIST_STATE)
    title = CharField(max_length=120, blank=True, null=True, unique=True)
    slug = SlugField(max_length=120, unique=True,
                     db_index=True, null=True, blank=True)
    state = IntegerField(default=0, choices=LIST_STATE)
    description = TextField(null=True)
    tags = ManyToManyField(Tag)
    picture = models.ImageField(null=True, upload_to="articles/")
    category = ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_article', kwargs={'slug': self.slug})
