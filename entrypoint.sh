#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate
python manage.py collectstatic --no-input --clear
if [-e "media/new_data.json"]
then
    python manage.py loaddata media/new_data.json
fi




#echo "*       *       *       *       *       /usr/local/bin/python /usr/src/app/manage.py process_subscriptions" >> /etc/crontabs/root
#crontab -l
#crond

exec "$@"
