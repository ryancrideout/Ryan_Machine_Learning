# Generated by Django 4.0.4 on 2022-08-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0014_alter_match_finished_alter_match_lobby_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='opened',
            field=models.BigIntegerField(null=True),
        ),
    ]