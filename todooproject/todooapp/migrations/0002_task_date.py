# Generated by Django 3.2.15 on 2022-10-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-23'),
            preserve_default=False,
        ),
    ]
