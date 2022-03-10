sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql
alter user postgres PASSWORD 'admin';
CREATE DATABASE frogie_cloudos_database;
\q
sudo -u postgres psql frogie_cloudos_database

BEGIN;


CREATE TABLE IF NOT EXISTS public.files
(
    file_name text NOT NULL,
    file_size bigint NOT NULL,
    id bigint NOT NULL,
    file_type text,
    PRIMARY KEY (id)
);
END;

sudo apt install libpq-dev python3-dev python3-pip unixodbc-dev
pip install psycopg2-binary
pip install psycopg2
pip install pyodbc

sudo crontab -e
@reboot python3 /home/Cloudos/server.py &
sudo ufw allow from any to any port 8000 proto tcp