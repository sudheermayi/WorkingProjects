# Generated by Django 3.1.7 on 2021-03-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc_app', '0002_toolconfiguration_projectname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tools',
            old_name='toolNname',
            new_name='toolName',
        ),
    ]
