# Generated by Django 4.0 on 2022-01-01 22:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True, unique=True)),
                ('head_line', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles/')),
                ('resume_link', models.CharField(blank=True, max_length=200, null=True)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
                ('linkdin_link', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=200, null=True)),
                ('website_link', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.BooleanField(choices=[(True, 'Activate'), (False, 'Deactivated')], default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
