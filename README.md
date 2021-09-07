
docker-compose up

docker-compose run web python3 ./manage.py makemigrations<br>
docker-compose run web python3 ./manage.py migrate<br>
docker-compose run web python3 ./manage.py createsuperuser --username admin --email admin@local.local<br>

docker-compose run web python3 ./manage.py shell -c 'from tiger import tasks; tasks.download_states.delay(); tasks.download_contressionaldistricts.delay(); tasks.download_urbanareas.delay(); tasks.download_counties.delay()'<br>
docker-compose run web python3 ./manage.py shell -c 'from uscensus import tasks; tasks.download_census_data.delay(True)'<br>
docker-compose run web python3 ./manage.py shell -c 'from kaggle_election import tasks; tasks.import_election2020.delay(True)'<br>
docker-compose run web python3 ./manage.py shell -c 'from nytcoviddata import tasks; tasks.import_national.delay(True); tasks.import_states.delay(True); tasks.import_counties.delay(True)'<br>
