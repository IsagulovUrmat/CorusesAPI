# Generated by Django 3.2.7 on 2021-09-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20210922_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='course.branch'),
        ),
        migrations.AlterField(
            model_name='course',
            name='contacts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='course.contact'),
        ),
    ]
