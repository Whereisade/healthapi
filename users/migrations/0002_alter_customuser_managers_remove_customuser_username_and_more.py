# Generated by Django 5.1.4 on 2025-01-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
