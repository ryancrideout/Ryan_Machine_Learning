# Generated by Django 4.0.4 on 2022-08-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoe2net_database', '0007_alter_match_cheats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='full_tech_tree',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
