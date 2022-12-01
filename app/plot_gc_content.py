import numpy as np
import matplotlib.pyplot as plt
import random
from config import APP_DIR


IMAGES_DIR = f"{APP_DIR}/gc-content_ratios"


def plot_gc_content_ratio(
    genomic_data: str, 
    step: int = 100, 
    outdir_name: str = f"{IMAGES_DIR}/",
    outfile_name: str = f"gc-content.png", 
    figsize: tuple = (8, 6),
    fontsize: int = 14,
    linewidth: int = 3,
    linecolor: str = "indigo"
    ):

    """
       A function that 
       (1) analyzes if the input sequence is correct, i.e.
           contains only DNA bases 'A', 'T', 'G' and 'C'.
           * If the input is incorrect, returns False and 
           prints the info about an incorrect input.
           * If the input is correct:
             (2) calculates CG-content ratio for each of
                 the 'step' segments of the molecule, which DNA sequence
                 is given in the 'genomic_data' parameter and
             (3) plots the GC ratio and saves the graph to image file

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

        Returns: 
            * True if the input sequence is correct,
            * False, otherwise. No plot is produced
    """

    # convert input sequence to uppercase if lowercase is provided 
    genomic_data = genomic_data.upper()

    # check the correctness of the input sequence
    # --------------------------------------------------------    
    a = genomic_data.count("A")
    t = genomic_data.count("T")
    g = genomic_data.count("G")
    c = genomic_data.count("C")

    if a + t + g + c != len(genomic_data):
        print("Input sequence is incorrect! Plot is not produced!")
        return False


    # calculate gc-content ratio
    # --------------------------------------------------------
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


    # plot gc-content ratio
    # --------------------------------------------------------
    plt.figure(figsize = figsize)
    plt.plot(genome_position,
             gc_content,
             color = linecolor,
             linewidth = linewidth)
    plt.xlabel("Genome position", fontsize = fontsize)
    plt.ylabel("GC-content, %", fontsize = fontsize)
    plt.xticks(fontsize = fontsize)
    plt.yticks(fontsize = fontsize)
    plt.savefig(f"{outdir_name}/{outfile_name}")
    plt.close()

    return True


# *** Some examples: ***

# (1) Plot GC-content distribution for the random DNA sequence
# dna_bases = ["A", "G", "C", "T"]
# genome = ""
# for i in range(10000):
#     base = random.choice(dna_bases)
#     genome += base

# plot_gc_content_ratio(genome)


# # (2) Plot the GC-content distribution for the SARS-CoV-2 genome
# # source: https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/2697049/
# covid_genome = ""
# with open("./covid/ncbi_dataset/data/genomic.fna", "r") as dataset:
#     first_line = True
#     for line in dataset.readlines():
        
#         # Skip dataset header
#         if first_line:
#             first_line = False
#             continue
#         covid_genome += line.replace("\n", "")

# plot_gc_content_ratio(covid_genome, outfile_name = "Corona.png")
