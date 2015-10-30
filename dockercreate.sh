#!/bin/bash

docker build -t ddjj/python   .
docker run --name ddjj-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=ddjj_db -d mysql:5.6

cp ./admin_ddjj/local_settings.py.example ./admin_ddjj/local_settings.py
docker run --rm --link ddjj-mysql:mysql -v $PWD:/admin_ddjj ddjj/python sh -c 'python manage.py syncdb --noinput && python manage.py migrate'
docker run -ti -p 8000  --name ddjj-python --link ddjj-mysql:mysql -v $PWD:/admin_ddjj ddjj/python /bin/bash

