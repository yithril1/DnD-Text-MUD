# Generated by Django 2.0.2 on 2018-04-03 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_guildskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='subrace',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='game.SubRace'),
        ),
    ]