# Generated by Django 2.2.9 on 2020-07-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_blacklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blacklist',
            old_name='list',
            new_name='username',
        ),
        migrations.AddField(
            model_name='blacklist',
            name='flag1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='flag2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='flag3',
            field=models.BooleanField(default=False),
        ),
    ]
