# Generated by Django 5.1.3 on 2024-11-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='Blog_image')),
                ('vedio', models.FileField(null=True, upload_to='Blog_vedio')),
                ('audio', models.FileField(null=True, upload_to='Blog_audio')),
                ('hashtag', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]