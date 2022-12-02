import os

#Install postgresql server: uncomment the following lines to install
os.system("sudo apt-get -y -qq update")
os.system("sudo apt-get -y -qq install postgresql")
os.system("sudo service postgresql start")

# Setup a password `postgres` for username `postgres`
os.system("sudo -u postgres psql -U postgres -c \"ALTER USER postgres PASSWORD 'postgres';\"")

# Setup a database with name `tfio_demo` to be used
os.system("sudo -u postgres psql -U postgres -c 'DROP DATABASE IF EXISTS geneticdb;'")
os.system("sudo -u postgres psql -U postgres -c 'CREATE DATABASE geneticdb;'")
