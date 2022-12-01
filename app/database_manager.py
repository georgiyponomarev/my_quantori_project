import json
from config import DB_URI, APP_DIR
from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine(DB_URI)
Base = declarative_base()


""" Create four tables:  
    (1, 2) with DNA and RNA bases, (3) with codons and 
    (4) with aminoacids 
"""
#------------------------------------------------------------
class BasesDNA(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    rna_id = Column(Integer, ForeignKey("rna_bases.id"))
    dna_base = Column(String(1))
    rna_base = relationship("BasesRNA", back_populates="dna_base")

    def __str__(self):
        dna_base, id, rna_id = self.dna_base, self.id, self.rna_id
        return f"DNA base {dna_base}: id = {id}, RNA base id = {rna_id}"


class BasesRNA(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    rna_base = Column(String(1))
    dna_base = relationship("BasesDNA", back_populates="rna_base")

    def __str__(self):
        return f"RNA base {self.rna_base}: id = {self.id}"


class Codons(Base):
    __tablename__ = "codons"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    triplet = Column(String(3))
    aminoacid = relationship("AminoAcids", back_populates="codon")
    aminoacid_id = Column(Integer, ForeignKey("aminoacids.id"))

    def __str__(self):
        triplet, id, aminoacid_id = self.triplet, self.id, self.aminoacid_id 
        return f"Codon {triplet}: id = {id}, aminoacid id = {aminoacid_id}"


class AminoAcids(Base):
    __tablename__ = "aminoacids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    aminoacid_letter = Column(String(1))
    codon = relationship("Codons", back_populates="aminoacid")

    def __str__(self):
        return f"Amino acid {self.aminoacid_letter}: id = {self.id}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)


# Fill the tables
#------------------------------------------------------------
dna_bases = ["A", "G", "C", "T"]
rna_bases = ["A", "G", "C", "U"]

# load genetic code from file
with open(f'{APP_DIR}/data/genetic_code.json', 'r') as json_file:
    genetic_code = json.load(json_file)

amino_acids = []
for first in rna_bases:
    for second in rna_bases:
        for third in rna_bases:
            amino_acid = genetic_code[first][second][third]
            amino_acids.append(amino_acid)

amino_acids = set(amino_acids)


with Session() as session:

    # fill the tables with DNA and RNA bases
    for r_base, d_base in zip(rna_bases, dna_bases):
        rna_base_ = BasesRNA(rna_base = r_base)
        session.add(rna_base_)
        dna_base_ = BasesDNA(dna_base = d_base, rna_base = rna_base_)
        session.add(dna_base_)

    # fill the table with amino acids
    for acid in amino_acids:
        amino_acid = AminoAcids(aminoacid_letter = acid)
        session.add(amino_acid)

    # fill the table with codons
    for first in rna_bases:
        for second in rna_bases:
            for third in rna_bases:

                triplet = first + second + third
                letter = genetic_code[first][second][third]

                query = session.query(
                    AminoAcids.id, 
                    AminoAcids.aminoacid_letter
                    ).filter(
                        AminoAcids.aminoacid_letter == letter
                        ).all()

                aminoacid_id = query[0][0]

                codon = Codons(triplet = triplet, aminoacid_id = aminoacid_id)
                session.add(codon)

    # add entries to database  
    session.commit()
