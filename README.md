
docker-compose up

docker exec -it -u $(id -u) covid-geogit_django_1 sh
      ./manage.py makemigrations
      ./manage.py migrate
      ./manage.py createsuperuser

./manage.py shell -c 'from tiger import tasks; tasks.download_states.delay(); tasks.download_contressionaldistricts.delay(); tasks.download_urbanareas.delay(); tasks.download_counties.delay()'


./manage.py importcsv --model='nytcoviddata.US' /data/scratch/covid-19-data/us.csv
./manage.py importcsv --model='nytcoviddata.State' /data/scratch/covid-19-data/us-states.csv
./manage.py importcsv --model='nytcoviddata.County' /data/scratch/covid-19-data/us-counties.csv


./manage.py importcsv --model='kaggle_election.PresidentCounty2020' /data/scratch/president_county_candidate.csv
