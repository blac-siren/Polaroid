# Generated by Django 2.1.5 on 2019-02-05 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20190205_1837'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserModel',
        ),
    ]
