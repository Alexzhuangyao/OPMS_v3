# Generated by Django 2.0.6 on 2018-07-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermanageuserrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermanageuserrecord',
            options={'verbose_name': '用户操作记录', 'verbose_name_plural': '用户操作记录'},
        ),
        migrations.RenameField(
            model_name='userlogininfo',
            old_name='agnet',
            new_name='agent',
        ),
    ]
