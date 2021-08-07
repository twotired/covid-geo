
docker-compose up

docker exec -it -u $(id -u) covid-geogit_django_1 bash
      ./manage.py makemigrations
      ./manage.py migrate
      ./manage.py createsuperuser

./manage.py shell -c 'from tiger import tasks; tasks.download_states.delay(); tasks.download_contressionaldistricts.delay(); tasks.download_urbanareas.delay(); tasks.download_counties.delay()'