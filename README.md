# qpa_final_project
Quantori Python Academy project

**Brief description of the project**
A set of tools for processing and analysis of the genomic data.
Namely, the tools for:
* DNA to RNA trancription, 
* RNA to protein translation
* Creating plots of GC-content ratio in a given DNA sequence

**ToDo!!!** 
Pack an app to Docker container and create a container with PostgreSQL database.
Run the app in Docker
:(

**How the project looks like at the moment (01/12/2022 6:00 AM):**
* The project root contains README.md, LICENSE, .gitignore and the folder with the app
* <ins>The 'app' folder</ins> contains:
    **Code files:**
    * config.py -- contains a path to a folder with the app and a database URI
    * configure_postgresql.py -- (a temporary file) which installs (if not) 
      postgresql and creates a database
    * database_manager.py -- a program which creates four tables in a database:
                             1. a table with dna bases
                             2. a table with rna bases
                             3. a table with codons
                             4. a table with amino acids
    * 
    
