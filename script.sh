#!/bin/bash
# Default IP and port
IP="0.0.0.0"
PORT="8000"
# Check if IP and port are passed as arguments
if [ ! -z "$1" ]; then
  IP=$1
fi

if [ ! -z "$2" ]; then
  PORT=$2
fi

# Navigate to the Django project directory
cd AugustaCRM || exit
# Run Django server
echo "making migrations"
python manage.py makemigrations
echo "migrating"
python manage.py migrate
echo "Running Django server on ${IP}:${PORT}"
python manage.py runserver $IP:$PORT