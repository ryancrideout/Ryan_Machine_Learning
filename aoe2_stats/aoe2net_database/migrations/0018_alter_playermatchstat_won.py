# Generated by Django 4.0.4 on 2022-08-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0017_alter_match_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatchstat',
            name='won',
            field=models.BooleanField(null=True),
        ),
    ]
