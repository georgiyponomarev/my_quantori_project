import json
import os


def genetic_code_to_json():
    """
      This function generates json file with genetic code 
      and directory "data" in the project root.

      The code is then read from the generated file 
      and used by the function "convert_rna_to_protein".
    """

    genetic_code = {
        "U":{ 
            "U":{"U":"F", "C":"F", "A":"L", "G":"L"},
            "C":{"U":"S", "C":"S", "A":"S", "G":"S"},
            "A":{"U":"Y", "C":"Y", "A":".", "G":"."},
            "G":{"U":"C", "C":"C", "A":".", "G":"W"}
        },
        "C":{
            "U":{"U":"L", "C":"L", "A":"L", "G":"L"},
            "C":{"U":"P", "C":"P", "A":"P", "G":"P"},
            "A":{"U":"H", "C":"H", "A":"Q", "G":"Q"},
            "G":{"U":"R", "C":"R", "A":"R", "G":"R"}
        },
        "A":{
            "U":{"U":"I", "C":"I", "A":"I", "G":"M"},
            "C":{"U":"T", "C":"T", "A":"T", "G":"T"},
            "A":{"U":"N", "C":"N", "A":"K", "G":"K"},
            "G":{"U":"S", "C":"S", "A":"R", "G":"R"}
        },
        "G":{
            "U":{"U":"V", "C":"V", "A":"V", "G":"V"},
            "C":{"U":"A", "C":"A", "A":"A", "G":"A"},
            "A":{"U":"D", "C":"D", "A":"E", "G":"E"},
            "G":{"U":"G", "C":"G", "A":"G", "G":"G"}
        }
    }

    try:
        os.mkdir("./data")
    except:
        print("The directory 'data' already exists")

    with open("./data/genetic_code.json", "w") as code_json:
        json.dump(genetic_code, code_json)


genetic_code_to_json()