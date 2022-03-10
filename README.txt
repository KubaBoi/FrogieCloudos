sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
apt show postgresql
sudo -u postgres psql
psql
alter user postgres PASSWORD 'admin';
ALTER ROLE
CREATE DATABASE frogie__cloudos_database;
\q
sudo -u postgres psql frogie_cloudos_database

sudo apt install libpq-dev python3-dev
sudo pip install psycopg2-binary
sudo pip install psycopg2
sudo apt install unixodbc-dev
sudo pip install pyodbc

sudo crontab -e
@reboot python3 /home/Cloudos/server.py &
sudo ufw allow from any to any port 8000 proto tcp