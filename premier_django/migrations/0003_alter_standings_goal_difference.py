# Generated by Django 5.1.2 on 2024-11-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_django', '0002_rename_adress_club_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standings',
            name='goal_difference',
            field=models.IntegerField(default=0),
        ),
    ]