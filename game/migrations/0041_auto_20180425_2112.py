# Generated by Django 2.0.2 on 2018-04-26 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0040_ability_cooldown'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharGuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('is_main', models.BooleanField(default=0)),
                ('stat', models.CharField(max_length=20)),
                ('statlevel', models.IntegerField(default=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Character')),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Guild')),
            ],
        ),
        migrations.CreateModel(
            name='CharSubGuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Character')),
                ('subguild', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.SubGuild')),
            ],
        ),
        migrations.RemoveField(
            model_name='bard',
            name='subguild',
        ),
        migrations.AddField(
            model_name='ability',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Bard',
        ),
    ]
