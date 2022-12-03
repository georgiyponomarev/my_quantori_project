# qpa_final_project
Quantori Python Academy project

**Brief description of the project**

The app which provides a set of tools for processing and analysis of the genomic data.
Namely, the tools for:

* DNA to RNA trancription, 
* RNA to protein translation
* Creating plots of GC-content ratio in a given DNA sequence

---

**How to use (some examples)**

1. `docker compose up -d --build`  -- create and start the containers with the app (named "genetic_tool") and postgres database
2. `docker exec -it genetic_tool [command]` -- execute commands within the container "genetic_tool"

[command] -- execute python scripts (or run some linux commands, etc.) 

3. `python database_manager.py` -- create a database and fill the tables. Must be executed the first, after the start of the containers 
4. `python run.py [option] [parameters]`

`[option]` must be one of the following: `convert, plot, test, help`

`[parameters]` are described in detail in `./app/doc/run_help.txt`

5. `docker compose down` -- stop the containers

---

**Examples:**

* `python run.py convert dna2rna "AGCT"` -- the input DNA sequence will be read from the command line
                                                  and the output RNA will be printed to stdout

* `python run.py convert rna2protein -f [path-to-rna-input-file] -o [path-to-protein-output-file]`
   in this case, the input RNA sequence is read from file and the output protein sequence is written to another file                                     

* `python run.py plot [path-to-input-file-with-DNA] [output-image-name]`

  `python run.py plot ./covid/ncbi_dataset/data/genomic.fna covid_test_plot.png` -- read the Covid-19 genetic code
    from file and save the image with the GC-content plot to .png file (by default the images are saved to ./app/gc-content_ratios) 

* `python run.py test converters` -- perform unit-tests for converter functions

* `python run.py test plotter` -- perform unit-test for plotter function

* `python run.py help` -- open the documentation for run.py script in *less* text viewer

---

**The project root directory contains:** 
* *files:* `docker-compose.yml, README.md, LICENSE, .gitignore` 
* *folders:* `database` (with the lonely Dockerfile) and `app`

The folder `app` contains:

*Python files:*    

* `config.py` -- contains a path to a folder with the app and a database URI
* `database_manager.py` -- a program which creates four tables in a database:
                             1. a table with dna bases
                             2. a table with rna bases
                             3. a table with codons
                             4. a table with amino acids
* `run.py` -- main script which runs different functions (see the documentation
                for run.py in ./app/doc/run_help.txt or by executing:
                `python run.py help`)
* `converters.py` -- contains functions for dna-to-rna, rna-to-protein and dna-to-protein
                       conversion
* `plot_gc_content.py` -- contains a function which plots GC-content ratio
* `test_converters.py` and `test_plotter.py` -- for unit-testing of the aforementioned functions

*Folders:*

* `covid` -- contains the Covid-19 genome (from https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/2697049/)
* `data` -- contains sqlite database and a json-file with a genetic code used to generate tables 
* `doc` -- contains the documentation for the main script run.py
* `gc-content_ratios` -- a folder where the plots are saved
* `legacy` -- a folder with old versions of the code files
* `tests` -- a folder with the test data 

*Dockerfile*
