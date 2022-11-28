from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_manager import (
    BasesDNA, BasesRNA, Codons, AminoAcids
)


def convert_dna_to_rna(dna_sequence) -> str:
    """
      Function that converts input DNA sequence,
      given as a string, to RNA sequence, 
      returned as a string as well. 
    """

    engine = create_engine(DB_URI)
    Session = sessionmaker(bind = engine)

    rna_sequence = ""
    for base in dna_sequence:
        with Session() as session:
            query = session.query(BasesDNA).filter(BasesDNA.dna_base == base) 
            for entry in query:
                rna_id = entry.rna_id
            rna_base = session.query(BasesRNA).get(rna_id)
            rna_sequence += rna_base.rna_base

    return rna_sequence


def convert_rna_to_protein(rna_sequence) -> str:
    """
      Function that converts input RNA sequence,
      given as a string, to protein sequence, 
      returned as a string as well. 
    """

    engine = create_engine(DB_URI)
    Session = sessionmaker(bind = engine)

    protein_sequence = ""

    for base in range(0, len(rna_sequence), 3):
        with Session() as session:
            codon = rna_sequence[base:base+3]
            if len(codon) == 3:
                query = session.query(Codons).filter(Codons.triplet == codon).all()
                aminoacid_id = query[0].aminoacid_id
                aminoacid = session.query(AminoAcids).get(aminoacid_id)
                protein_sequence += aminoacid.aminoacid_letter

    return protein_sequence

