# Generated by Django 4.2.10 on 2024-03-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='current_members_count',
            field=models.IntegerField(default=0),
        ),
    ]
