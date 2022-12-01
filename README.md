# qpa_final_project
Quantori Python Academy project

**Brief description of the project**
A set of tools for processing and analysis of the genomic data.
Namely, the tools for:
* DNA to RNA trancription, 
* RNA to protein translation
* Creating plots of GC-content ratio in a given DNA sequence

**How to use (some examples)**
1. run the `configure_postgresql.py` and `database_manager.py` to set up
   a database (needed only at the first run; *Task 2*)
2. run `python ./app/run.py` in terminal with command line arguments (*Task 4*):
   
**Task 1 examples:**  
* `python ./app/run.py convert dna2rna "AGCT"` -- the input DNA sequence will be read from the command line
                                                  and the output RNA will be printed to stdout
* `python ./app/run.py convert rna2protein -f (path-to-rna-input-file) -o (path-to-protein-output-file)`
   in this case, the input RNA sequence is read from file and the output protein sequence is written to another file                                     

**Task 3 example:**
*  `python ./app/run.py plot ./app/covid/ncbi_dataset/data/genomic.fna covid_test_plot.png` -- read the Covid-19 genetic code
    from file and save the image with the GC-content plot to .png file (by default the images are saved to ./app/gc-content_ratios) 

**Task 5 examples:**
* `python ./app/run.py test converters` -- perform unit-tests for converter functions
* `python ./app/run.py test converters` -- perform unit-test for plotter function

**Call for help**
* `python ./app/run.py help`*

---

**ToDo!!!** 
Pack an app to Docker container and create a container with PostgreSQL database.
Run the app in Docker
:(

**How the project looks like at the moment (01/12/2022 6:00 AM):**
* The project root contains README.md, LICENSE, .gitignore and the folder with the app
* The 'app' folder  contains:

    **Code files:**
    * run.py -- main script which runs different functions (see the documentation
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

    **Folders:**
    * covid -- contains the Covid-19 genome (from https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/2697049/)
    * data -- contains sqlite database and a json-file with a genetic code used to generate tables 
    * doc -- contains file with the documentation of the main script run.py
    * gc-content_ratios -- a folder where the plots are saved
    * legacy -- a folder with old versions of the code files
    * tests -- a folder with the test data 
    
    **Dockerfile** -- now it is waiting for its finest hour... :(
    
