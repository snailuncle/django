# Generated by Django 2.0.3 on 2018-04-25 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180425_0917'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailVerfyRecord',
            new_name='EmailVerifyRecord',
        ),
    ]
