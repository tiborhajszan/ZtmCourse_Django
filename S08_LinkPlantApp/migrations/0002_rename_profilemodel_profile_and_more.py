# Generated by Django 4.2.16 on 2024-11-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('S08_LinkPlantApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileModel',
            new_name='Profile',
        ),
        migrations.RenameModel(
            old_name='LinkModel08',
            new_name='S08Link',
        ),
    ]
