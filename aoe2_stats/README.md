## Running Django

To run Django, simply launch this command:

```python manage.py runserver```

## Accessing the Database

To actually run the web application of `pgAdmin` and access the database, you'll need to run the `pgAdmin` Python file. For me this looks like:

```python "G:\\PostgreSQL\pgAdmin 4\web\pgAdmin4.py"```

But in short, you want to be executing the `pgAdmin4.py` file.

## General Database Installation Instructions

Instructions are based on [this tutorial.](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)

1. Go and install PostGres and place it wherever you like.
2. When creating the database, be sure to call it `aoe2net_database`. If not, you'll have to change the settings files to accomodate.
3. Set the `pg_hba.conf` permissions to be 'trust'. This normally isn't recommended, but this is publicly available data so it should be okay. Note that this file will live somewhere like `Postgres/14/data/pg_hba.conf` or something of that nature.
4. That should be all. Note that the database lives on localhost:5050.

## Getting Started

1. First order of business will be installing the Pipenv environment. To accomplish this, you want to be in the `Ryan_Machine_Learning` directory, and then you simply run `pipenv install`. This will install the required libraries. Note that you'll also need to be on Python version 3.
2. Then, run `pipenv shell` to activate the virtual environment. From here, you'll be able to run Python scripts willy-nilly. If you've installed the Database and Django already, then you're done. If not, you'll have to do that.
3. To install the Database, see the above instructions - `General Database Installation Instructions`.

TODO: Fill this out more. How do we install Django?

## Relevant Links

These are some potentially useful links for this project - most notably we pull data from `https:aoe2.net/`, but the other links could be good reference points.

Website: https://www.ageofstatistics.com/statistics/criteria?game=aoe2&period=p03_v01&filter=rm_solo_all

Github Repository: https://github.com/gowerc/age-of-statistics

Account on Reddit: https://www.reddit.com/user/coolio9876/

Source of Data: https://aoe2.net/#

### Predictive Behaviour Modelling Links

These links can be helpful in determining how to do predictive analysis on the dataset I hope to collect.
- https://www.section.io/engineering-education/applying-ai-and-ml-to-predict-consumer-behavior/
- https://builtin.com/machine-learning/predictive-behavior-modeling
- https://www.mathworks.com/discovery/predictive-modeling.html (This has links to other resources it looks like)
- https://www.sas.com/en_gb/insights/articles/analytics/a-guide-to-predictive-analytics-and-machine-learning.html
