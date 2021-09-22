# Generated by Django 3.2.7 on 2021-09-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('staff', 'STAFF'), ('student', 'STUDENT'), ('teacher', 'TEACHER')], default='admin', max_length=15),
            preserve_default=False,
        ),
    ]
