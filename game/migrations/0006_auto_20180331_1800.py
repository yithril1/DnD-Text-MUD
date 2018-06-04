# Generated by Django 2.0.2 on 2018-03-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_race_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='subguild',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subrace',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='guild',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='spell',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]