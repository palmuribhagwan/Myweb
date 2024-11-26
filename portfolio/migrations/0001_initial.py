# Generated by Django 2.1.7 on 2024-09-04 06:19

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.TextField()),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('paragaph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('moble_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.TextField(blank=True, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.TextField()),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contact_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='desktop_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='desktop')),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.TextField()),
                ('Degree', models.TextField()),
                ('Branch', models.CharField(blank=True, max_length=50, null=True)),
                ('university', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='email_host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recive_mail_to', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.TextField()),
                ('company', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('mail', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('linkedin_link', models.TextField(blank=True, null=True)),
                ('insta_link', models.TextField(blank=True, null=True)),
                ('github_link', models.TextField(blank=True, null=True)),
                ('whatsapp_No', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='home_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='home_pgh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='main_head_achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('moble_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.TextField(blank=True, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='main_head_certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('moble_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.TextField(blank=True, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='main_head_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('moble_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.TextField(blank=True, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mobile_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Nav_Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Blogs', models.BooleanField()),
                ('Resume', models.BooleanField()),
                ('Projects', models.BooleanField()),
                ('certificates', models.BooleanField()),
                ('Achievements', models.BooleanField()),
                ('contact', models.BooleanField()),
                ('search', models.BooleanField()),
                ('header_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('sidebar_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pop_Name', models.CharField(max_length=50)),
                ('popup_message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('view_imgvid_left', models.BooleanField(default=False)),
                ('view_imgvid_Right', models.BooleanField(default=True)),
                ('project_title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('outcome', models.TextField(blank=True, null=True)),
                ('ul_head', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('source_code', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='project_ul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_context', models.TextField()),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='portfolio.project')),
            ],
        ),
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.experience')),
            ],
        ),
        migrations.CreateModel(
            name='resume_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.TextField(blank=True, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='resume')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill_title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='portfolio.Skill_title'),
        ),
    ]
