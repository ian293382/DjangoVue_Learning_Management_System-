# Generated by Django 5.0 on 2024-01-07 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]