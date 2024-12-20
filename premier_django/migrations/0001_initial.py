# Generated by Django 5.1.2 on 2024-10-26 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('club_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('founded', models.DateField()),
                ('coach', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stadium',
            fields=[
                ('stadium_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='club_logo',
            fields=[
                ('club_logo_id', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='club_logos/')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.club')),
            ],
        ),
        migrations.CreateModel(
            name='match_info',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('home_team_goals', models.IntegerField()),
                ('away_team_goals', models.IntegerField()),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='premier_django.club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='premier_django.club')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.stadium')),
            ],
        ),
        migrations.CreateModel(
            name='assist',
            fields=[
                ('assist_id', models.AutoField(primary_key=True, serialize=False)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.match_info')),
            ],
        ),
        migrations.CreateModel(
            name='match_statictic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possession_home', models.IntegerField()),
                ('possession_away', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.match_info')),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('sign_contract_date', models.DateField()),
                ('contract_expired', models.DateField()),
                ('current_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.club')),
            ],
        ),
        migrations.CreateModel(
            name='goal',
            fields=[
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('goal_time', models.IntegerField()),
                ('goal_type', models.CharField(max_length=100)),
                ('assist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assist', to='premier_django.assist')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.match_info')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.player')),
            ],
        ),
        migrations.AddField(
            model_name='assist',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.player'),
        ),
        migrations.CreateModel(
            name='player_stats',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_goals', models.IntegerField()),
                ('player_assists', models.IntegerField()),
                ('player_yellow_cards', models.IntegerField()),
                ('player_red_cards', models.IntegerField()),
                ('player_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.player')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='stadium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.stadium'),
        ),
        migrations.CreateModel(
            name='standings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('goals_scored', models.IntegerField()),
                ('goals_conceded', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('points', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premier_django.club')),
            ],
        ),
    ]
