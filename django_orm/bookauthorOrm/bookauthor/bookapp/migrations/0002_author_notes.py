# Generated by Django 2.2.4 on 2021-05-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
