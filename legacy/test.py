from script import convert_dna_to_rna, convert_rna_to_protein


# Test data for the functions
input_dna = [
    "ATTTGGCTACTAACAATCTA",
    "GTTGTAATGGCCTACATTA", 
    "CAGGTGGTGTTGTTCAGTT",
    "GCTAACTAAC",
    "GCTAACTAACATCTTTGGCACTGTT",
    "TATGAAAAACTCAAA",
    "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"
]

correct_rna = [
    "AUUUGGCUACUAACAAUCUA",
    "GUUGUAAUGGCCUACAUUA",
    "CAGGUGGUGUUGUUCAGUU",
    "GCUAACUAAC",
    "GCUAACUAACAUCUUUGGCACUGUU",
    "UAUGAAAAACUCAAA",
    "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
]

correct_protein = [
    "IWLLTI",
    "VVMAYI",
    "QVVLFS",
    "AN.",
    "AN.HLWHC",
    "YEKLK",
    "PVLDWLEEKF"
]


def test_function(function, input_seq, output_seq):
    """
        Check if the functions output correct results 
    """

    print(f"Testing function {function.__name__}:")
    failed_tests = 0
    for test_in, test_out in zip(input_seq, output_seq):
        result = function(test_in)
        try:
            assert result == test_out
        except AssertionError:
            failed_tests += 1
            print('*** Error! ***')
            print("result:", result)
            print("correct:", test_out)
            print()

    if failed_tests > 0:
        print("Failed", failed_tests, "tests out of", len(output_seq))
    else:
        print("All tests passed successfully\n")


test_function(convert_dna_to_rna, input_dna, correct_rna)
test_function(convert_rna_to_protein, correct_rna, correct_protein)
