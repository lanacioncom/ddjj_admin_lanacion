#!/bin/bash

if [ -z "$1" ]; then
    echo "dockerstart.sh [create|start|stop|bash|mysql|port|tmp]"
    exit
fi

if [ $1 == 'start' ]; then 
   docker start ddjj-mysql
   docker start -ai ddjj-python
   exit
fi

if [ $1 == 'stop' ]; then
   docker stop ddjj-python      
   docker stop ddjj-mysql
   exit
fi

if [ $1 == 'mysql' ]; then
   docker run -it --link ddjj-mysql:mysql -v $PWD:/admin_ddjj --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ROOT_PASSWORD"'    
   exit
fi

if [ $1 == 'bash' ]; then
   docker start -ai ddjj-python
   exit
fi

if [ $1 == 'tmp' ]; then
    docker run -it -p 8000  --rm --link ddjj-mysql:mysql -v $PWD:/admin_ddjj ddjj/python /bin/bash
   exit
fi


if [ $1 == 'port' ]; then 
   docker port ddjj-python
   exit
fi

echo "dockerstart.sh [create|start|stop|bash|mysql|port|tmp]"
