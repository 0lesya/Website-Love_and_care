# Generated by Django 4.1 on 2023-06-02 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment_delete_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
