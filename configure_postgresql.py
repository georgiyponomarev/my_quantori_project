from subprocess import call


def cmd(command: str):
    """ Execute linux commands """
    call(command, shell = True)


# Install postgresql server
cmd("sudo apt-get -y -qq update")
cmd("sudo apt-get -y -qq install postgresql")
cmd("sudo service postgresql start")

# Setup a password `postgres` for username `postgres`
cmd("sudo -u postgres psql -U postgres -c \"ALTER USER postgres PASSWORD 'postgres';\"")

# Setup a database with name `tfio_demo` to be used
cmd("sudo -u postgres psql -U postgres -c 'DROP DATABASE IF EXISTS geneticdb;'")
cmd("sudo -u postgres psql -U postgres -c 'CREATE DATABASE geneticdb;'")
