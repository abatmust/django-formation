# Generated by Django 4.0 on 2021-12-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tag_article_category_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='state',
            field=models.IntegerField(choices=[(0, 'disable'), (1, 'enable')], default=0),
        ),
    ]
