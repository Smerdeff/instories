# instories
Django AdminLTE example(nginx, gunicorn, postgres, docker)

### Install:
```
git clone https://github.com/smerdeff/instories.git
cd instories
docker-compose up
ctrl+break
docker-compose exec python python manage.py migrate --noinput
docker-compose exec python python manage.py collectstatic --noinput
docker-compose exec python python manage.py createsuperuser
```

http://localhost/admin/