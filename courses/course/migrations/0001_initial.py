# Generated by Django 3.2.7 on 2021-09-22 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=150)),
                ('longitude', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('imgpath', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ImageField(max_length=50, upload_to='')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('logo', models.CharField(max_length=150)),
                ('branches', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.branch')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category')),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.contact')),
            ],
        ),
    ]