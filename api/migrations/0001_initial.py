# Generated by Django 4.2.20 on 2025-03-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonImg', models.ImageField(upload_to='images/MeetOurTeam/')),
                ('NameOfPerson', models.CharField(max_length=100)),
                ('PositionOfPerson', models.CharField(max_length=100)),
                ('AboutPerson', models.TextField()),
                ('Icon1', models.CharField(max_length=100)),
                ('Icon2', models.CharField(max_length=100)),
                ('Icon3', models.CharField(max_length=100)),
                ('SocialLink1', models.URLField(max_length=300)),
                ('SocialLink2', models.URLField(max_length=300)),
                ('SocialLink3', models.URLField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogImg', models.ImageField(upload_to='images/Blogs/')),
                ('BlogTitle', models.CharField(max_length=100)),
                ('BlogDescription', models.TextField()),
                ('BlogFaculty', models.CharField(max_length=100)),
                ('BlogLink', models.URLField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LogoImg', models.ImageField(upload_to='images/')),
                ('HeroImg', models.ImageField(upload_to='images/HeroImg/')),
                ('HeroTitle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PortfolioImg', models.ImageField(upload_to='images/Portfolio/')),
                ('PortfolioTitle', models.CharField(max_length=100)),
                ('PortfolioLink', models.URLField(max_length=300)),
                ('PortfolioDescription', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceImg', models.ImageField(upload_to='images/Services/')),
                ('ServiceTitle', models.CharField(max_length=100)),
                ('ServiceTagLines', models.CharField(max_length=300)),
                ('WhoDO', models.CharField(max_length=150)),
                ('ServiceDescription', models.TextField()),
                ('Feature1', models.CharField(max_length=300)),
                ('Feature2', models.CharField(max_length=300)),
                ('Feature3', models.CharField(max_length=300)),
                ('Feature4', models.CharField(max_length=300)),
                ('Feature5', models.CharField(blank=True, max_length=300, null=True)),
                ('Feature6', models.CharField(blank=True, max_length=300, null=True)),
                ('Feature7', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
