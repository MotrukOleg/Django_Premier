# Generated by Django 5.1.2 on 2024-12-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_django', '0007_player_age_player_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_info',
            name='away_team_possession',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match_info',
            name='home_team_possession',
            field=models.IntegerField(default=0),
        ),
    ]
