# Generated by Django 5.1.1 on 2024-12-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamedata',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('winner_name', models.CharField(blank=True, default='winner', max_length=255)),
                ('loser_name', models.CharField(blank=True, default='loser', max_length=255)),
                ('winner_score', models.IntegerField(default=0)),
                ('loser_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournamentsdata',
            fields=[
                ('tournament_id', models.AutoField(primary_key=True, serialize=False)),
                ('winner_name', models.CharField(blank=True, default='user', max_length=255)),
                ('started', models.BooleanField(default=False)),
            ],
        ),
    ]
