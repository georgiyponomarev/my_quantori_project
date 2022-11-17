import numpy as np
import matplotlib.pyplot as plt
import random


def plot_gc_content_ratio(genome_position:np.array,
                  gc_content:np.array,
                  dataset = "random DNA sequence",
                  outfile = "gc-content.png",
                  figsize = (8, 6),
                  fontsize = 14,
                  linewidth = 3,
                  linecolor = "indigo"
                  ):

    """
       The function for plotting the GC-content ratio
       in a DNA sequence. 
       The resulting graph is saved to .png file

       In the graph:
           * x-axis: Genome position -- position of first base
                     in a bin
           * y-axis: GC-content ratio in %

      Input parameters:
           * genome_position and gc_content -- two numpy arrays, 
             used for creating the graph -- x and y(x), respectively
           * other parameters are intended to make the graph 
             prettier and more descriptive 
    """
    
    plt.figure(figsize = figsize)
    plt.plot(genome_position, 
             gc_content, 
             color = linecolor, 
             linewidth = linewidth)
    plt.title(f"Plot of the CG-content distribution in a {dataset}", fontsize = fontsize)
    plt.xlabel("Genome position", fontsize = fontsize)
    plt.ylabel("GC-content, %", fontsize = fontsize)
    plt.xticks(fontsize = fontsize)
    plt.yticks(fontsize = fontsize)
    plt.savefig(outfile)
    plt.close()


def gc_content_ratio(genomic_data:str, 
                     step:int = 100, 
                     dataset_name:str = "random DNA sequence",
                     outfile_name = "gc-content.png"
                     ):
    """
       A function that 
       (1) calculates CG-content ratio for each of
       the 'step' segments of the molecule, which DNA sequence
       is given in the 'genomic_data' parameter and
       (2) plots the GC ratio and saves the graph to image file,
       using external function 'plot_gc_content_ration'

       Input parameters:
          * genomic_data (string) -- a DNA sequence
          * step (int) -- denotes a width of a subsequence within
                          which the GC-content ratio is calculated.
                          By default bin width = 100 characters.
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

    plot_gc_content_ratio(genome_position, 
                          gc_content, 
                          dataset = dataset_name,
                          outfile = outfile_name)


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
                 outfile_name = "Corona.png" 
                )
