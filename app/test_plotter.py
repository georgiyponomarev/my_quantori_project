import os
import random
import unittest
from plot_gc_content import plot_gc_content_ratio


# Create folder with test plots
# ---------------------------------------------------
TEST_IMAGES_DIR = "./tests/gc-content_plots"
try:
    os.mkdir(TEST_IMAGES_DIR)
except FileExistsError:
    print(f"Folder {TEST_IMAGES_DIR} already exists")

"""
Prepare input test data: correct one contains only
letters which represent DNA bases: A, T, G, C
"""
# ---------------------------------------------------
dna_bases = "atgc"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


correct_input = ""
incorrect_input = ""
for i in range(1000):
    correct_input += random.choice(dna_bases)
    incorrect_input += random.choice(alphabet)


""" names of the output images: 
if the input is correct, an output image "test_correct.png" 
should be produced; 
if the input is incorrect, an output image "test_correct.png" 
should NOT be produced; 
"""
# ---------------------------------------------------
correct_output = "test_correct.png"
incorrect_output = "test_incorrect.png"


# create unit tests
# ---------------------------------------------------
class PlotterTest(unittest.TestCase):
    """
    The class for unit-testing the function
    that plots gc-content ratio. 

    The function is imported from the file "plot_gc_content.py".
    It create a plot and returns True if only the input is a 
    correct DNA sequence (does not contain any symbols except
    "A", "T", "G" and "C"; upper/lower-case does not matter)

    If the input is incorrect, no plot is produced and False 
    is returned.
    """

    def test_correct_input(self):
        print(f"Testing if the input data is correct")
        self.assertTrue(
            plot_gc_content_ratio(
                genomic_data = correct_input,
                outdir_name = f"{TEST_IMAGES_DIR}",
                outfile_name = f"{correct_output}"
            )
        )

    def test_incorrect_input(self):
        print(f"Testing if the function returns False given the input is incorrect")
        self.assertFalse(
            plot_gc_content_ratio(
                genomic_data = incorrect_input,
                outdir_name = f"{TEST_IMAGES_DIR}",
                outfile_name = f"{incorrect_output}"
            )
        )

    def test_image_exists_if_input_correct(self):
        print(f"Testing if the function produces image output given the correct input")
        imagedir = os.listdir(TEST_IMAGES_DIR)
        self.assertIn(correct_output, imagedir)

    def test_no_image_if_input_incorrect(self):
        print(f"Testing if the function produces no image output given the incorrect input")
        imagedir = os.listdir(TEST_IMAGES_DIR)
        self.assertNotIn(incorrect_output, imagedir)    	


# perform unit tests
# ---------------------------------------------------
if __name__ == '__main__':
    unittest.main()
