# Generated by Django 2.0.2 on 2018-04-05 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20180404_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subrace',
            name='race',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='game.Race'),
        ),
    ]
