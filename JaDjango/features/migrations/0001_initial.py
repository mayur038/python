# Generated by Django 5.0 on 2024-02-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExportCSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExportFile', models.FileField(default='null', upload_to='excel')),
            ],
        ),
    ]
