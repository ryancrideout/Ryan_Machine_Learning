# Generated by Django 4.0.4 on 2022-08-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0015_alter_match_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='started',
            field=models.BigIntegerField(null=True),
        ),
    ]
