# Generated by Django 5.0 on 2024-02-29 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_remove_cuser_username_cuser_id_alter_cuser_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuser',
            name='Email',
        ),
    ]
