## General Database Installation Instructions

Instructions are based on [this tutorial.](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)

1. Go and install PostGres and place it wherever you like.
2. When creating the database, be sure to call it 'aoe2net_database'. If not, you'll have to change the settings files to accomodate.
3. Set the `pg_hba.conf` permissions to be 'trust'. This normally isn't recommended, but this is publicly available data so it should be okay.
4. That should be all. Note that the database lives on localhost:5050.