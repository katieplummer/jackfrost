# Generated by Django 2.2.4 on 2020-03-12 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
    ]