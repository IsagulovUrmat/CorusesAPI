# Generated by Django 3.2.7 on 2021-09-22 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210922_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branches',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='course.branch'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='course.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='contacts',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='course.contact'),
        ),
    ]
