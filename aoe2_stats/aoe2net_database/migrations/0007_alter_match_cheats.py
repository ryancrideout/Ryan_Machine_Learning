# Generated by Django 4.0.4 on 2022-08-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0006_alter_match_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='cheats',
            field=models.BooleanField(default=False, null=True),
        ),
    ]