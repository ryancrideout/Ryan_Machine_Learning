# Generated by Django 4.0.4 on 2022-08-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0010_alter_match_lock_speed_alter_match_lock_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]