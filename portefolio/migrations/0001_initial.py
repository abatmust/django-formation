# Generated by Django 4.0 on 2022-01-01 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0008_alter_article_slug'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('source_link', models.CharField(blank=True, max_length=200)),
                ('demo_link', models.CharField(blank=True, max_length=200)),
                ('vote', models.IntegerField(default=1)),
                ('state', models.BooleanField(choices=[(True, 'Activate'), (False, 'Deactivated')], default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.profile')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
