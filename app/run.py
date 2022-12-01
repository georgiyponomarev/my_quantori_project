import random
import sys
from config import APP_DIR
from converters import (
    convert_dna_to_rna, convert_rna_to_protein, 
    convert_dna_to_protein    
)
from plot_gc_content import plot_gc_content_ratio
import os


# read command line arguments
# first one is run.py -- it is omitted
option, *args = sys.argv[1:]


def read_sequence(path_to_file: str) -> str:
    """ This function reads a sequence from
        text file and returns a string object, 
        containing the sequence. 
        The file is assumed to have a header line
        with short description
    """

    try:
        sequence = ""
        with open(f"{path_to_file}", "r") as dataset:
            first_line = True
            for line in dataset.readlines():

                # Skip dataset header 
                if first_line:
                    first_line = False
                    continue
                sequence += line.replace("\n", "")
        
        return sequence

    except FileNotFoundError:
        print(f"File {path_to_file} not found!")
        exit()


# run different tools
# ***************************************************************
# view help
if option == "help":
    os.system(f"less {APP_DIR}/doc/run_help.txt")


# ***************************************************************
# translate dna to rna or transcribe rna to protein
elif option == "convert":

    converters_aliases = {
        "convert_dna_to_rna": convert_dna_to_rna,
        "dna2rna" : convert_dna_to_rna,
        "convert_rna_to_protein": convert_rna_to_protein,
        "rna2protein" : convert_rna_to_protein,
        "convert_dna_to_protein": convert_dna_to_protein,
        "dna2protein" : convert_dna_to_protein
    }

    # check if a valid function alias is provided
    try:
        function_name = args[0]
        converter_function = converters_aliases[function_name]
    except KeyError:
        print("\nAn invalid function name is provided! Please, use one of the following:\n")
        for alias, function in converters_aliases.items():
            print(f"{alias}:   calls function '{function.__name__}'")
        print()

    # read DNA/RNA sequence from file
    if "-f" in args:
        path_to_file = args[2]
        if path_to_file == "-o":
            print("\n Error!") 
            print("The script was told to read the data from file but a path to file was not specified!\n")
            exit()
        sequence = read_sequence(path_to_file)
    else:
        """input sequence is provided directly from command-line"""
        sequence = args[1]
    
    # translation/transcription result (a string)
    result = converter_function(sequence)

    # if the output file is specified; 
    # print result to stdout otherwise 
    if "-o" in args:
        outfile = args[-1]
        if outfile != "-o":
            with open(f"{outfile}", "w") as output_file:
                # generate header
                output_file.write(f"The output from {converter_function.__name__}\n")

                # write resulting sequence to file
                output_file.write(result)
        else:
            print("The output file is not provided!")
            print(f"The result is {result}")
    else:
        print(result)


# ***************************************************************
# plot gc_content from file and save the plot to image
elif option == "plot":
    path_to_file, *outfile_name = args

    if not outfile_name:
        outfile_name = "gc-content.png"
    else:
        outfile_name = outfile_name[0]

    sequence = read_sequence(path_to_file)
    plot_gc_content_ratio(sequence, outfile_name = outfile_name)


# ***************************************************************
# test if the functions work correctly
elif option == "test":
    tests = {
        "converters": "test_converters.py", 
        "plotter": "test_plotter.py"
    }
    try:
        test_module = args[0]
        test_module = tests[test_module]
        os.system(f"python {APP_DIR}/{test_module}") 
    except KeyError:
        print(f"invalid parameter {args[0]} given. Try one of the following\n")
        for parameter, module in tests.items():
            print(f"use parameter {parameter} to run {module}")


# ***************************************************************
# exit if an invalid option is provided
else:
    print("an invalid option is provided. Exiting...")
    exit()

exit()
