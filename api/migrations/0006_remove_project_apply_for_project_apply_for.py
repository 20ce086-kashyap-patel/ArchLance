# Generated by Django 4.0.3 on 2022-04-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_project_apply_for_alter_project_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='apply_for',
        ),
        migrations.AddField(
            model_name='project',
            name='apply_for',
            field=models.ManyToManyField(to='api.architectureaccount'),
        ),
    ]