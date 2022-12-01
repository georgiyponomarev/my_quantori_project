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
* The 'app' folder  contains:

    **Code files:**
    * ***run.py*** -- main script which runs different functions (see the documentation
                      for run.py in ./app/doc/run_help.txt or by typing in the terminal:
                      `python ./app/run.py help`)    
    * config.py -- contains a path to a folder with the app and a database URI
    * configure_postgresql.py -- (a temporary file) which installs (if not) 
      postgresql and creates a database
    * database_manager.py -- a program which creates four tables in a database:
                             1. a table with dna bases
                             2. a table with rna bases
                             3. a table with codons
                             4. a table with amino acids
    * converters.py -- contains functions for dna-to-rna, rna-to-protein and dna-to-protein
                       conversion
    * plot_gc_content.py -- contains a function which plots GC-content ratio
    * test_converters.py, test_plotter.py -- for unit-testing of the aforementioned functions
    
