import numpy as np
import matplotlib.pyplot as plt
import random


IMAGES_DIR = "./gc-content_ratios"


def gc_content_ratio(
    genomic_data: str, 
    step: int = 100, 
    dataset_name: str = "random DNA sequence",
    outfile_name: str = IMAGES_DIR + "/gc-content.png", 
    figsize: tuple = (8, 6),
    fontsize: int = 14,
    linewidth: int = 3,
    linecolor: str = "indigo"
    ):

    """
       A function that 
       (1) calculates CG-content ratio for each of
       the 'step' segments of the molecule, which DNA sequence
       is given in the 'genomic_data' parameter and
       (2) plots the GC ratio and saves the graph to image file

       In the plot:
           * x-axis: Genome position -- position of first base
                     in a bin
           * y-axis: GC-content ratio in % 

       Input parameters:
          * genomic_data (string) -- a DNA sequence
          * step (int) -- denotes a width of a subsequence within
                          which the GC-content ratio is calculated.
                          By default bin width = 100 characters.
          * other parameters are intended to make the graph 
            prettier and more descriptive
    """

    molecule_length = len(genomic_data)
    number_of_bins = molecule_length // step
    gc_content = np.zeros(number_of_bins)
    genome_position = np.zeros(number_of_bins)

    index = 0
    for start_base in range(0, molecule_length, step):
        subseq = genomic_data[start_base: start_base + step]
        if len(subseq) % step == 0:
            g, c = subseq.count("G"), subseq.count("C")
            gc_content[index] = (g + c) / step * 100
            genome_position[index] = start_base
        index += 1

    plt.figure(figsize = figsize)
    plt.plot(genome_position,
             gc_content,
             color = linecolor,
             linewidth = linewidth)
    plt.title(f"Plot of the CG-content distribution in a {dataset_name}", fontsize = fontsize)
    plt.xlabel("Genome position", fontsize = fontsize)
    plt.ylabel("GC-content, %", fontsize = fontsize)
    plt.xticks(fontsize = fontsize)
    plt.yticks(fontsize = fontsize)
    plt.savefig(outfile_name)
    plt.close()


# *** Some tests ***
#
# (1) Plot GC-content distribution for the random DNA sequence
dna_bases = ["A", "G", "C", "T"]
genome = ""
for i in range(10001):
    base = random.choice(dna_bases)
    genome += base

gc_content_ratio(genome)


# (2) Plot the GC-content distribution for the SARS-CoV-2 genome
# source: https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/2697049/
covid_genome = ""
with open("./covid/ncbi_dataset/data/genomic.fna", "r") as dataset:
    first_line = True
    for line in dataset.readlines():
        
        # Skip dataset header
        if first_line:
            first_line = False
            continue
        covid_genome += line.replace("\n", "")

gc_content_ratio(covid_genome, 
                 dataset_name = "SARS-CoV-2 genome",
                 outfile_name = IMAGES_DIR + "/Corona.png" 
                )
