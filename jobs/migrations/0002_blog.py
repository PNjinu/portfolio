# Generated by Django 4.0.1 on 2022-02-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_cont', models.CharField(max_length=350)),
                ('blog_link', models.URLField()),
            ],
        ),
    ]
