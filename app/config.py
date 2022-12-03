db_name = 'geneticdb'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'db'
db_port = '5432'

# Connect to the database
DB_URI = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}" 

# Main folder with an
APP_DIR = "."