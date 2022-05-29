## Running Django

To run Django, simply launch this command:

```python manage.py runserver```

## Accessing the Database

To actually run the web application of `pgAdmin` and access the database, you'll need to run the `pgAdmin` Python file. For me this looks like:

```python "G:\\PostgreSQL\pgAdmin 4\web\pgAdmin4.py"```

## General Database Installation Instructions

Instructions are based on [this tutorial.](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)

1. Go and install PostGres and place it wherever you like.
2. When creating the database, be sure to call it `aoe2net_database`. If not, you'll have to change the settings files to accomodate.
3. Set the `pg_hba.conf` permissions to be 'trust'. This normally isn't recommended, but this is publicly available data so it should be okay. Note that this file will live somewhere like `Postgres/14/data/pg_hba.conf` or something of that nature.
4. That should be all. Note that the database lives on localhost:5050.

## Relevant Links

These are some potentially useful links for this project - most notably we pull data from `https:aoe2.net/`, but the other links could be good reference points.

Website: https://www.ageofstatistics.com/statistics/criteria?game=aoe2&period=p03_v01&filter=rm_solo_all

Github Repository: https://github.com/gowerc/age-of-statistics

Account on Reddit: https://www.reddit.com/user/coolio9876/

Source of Data: https://aoe2.net/#
