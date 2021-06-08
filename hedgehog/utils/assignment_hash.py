import hashlib
import collections
import csv
from Bio import SeqIO

def add_to_hash(seq_file):
    hash_map = {}
    seq_hash = {}
    for record in SeqIO.parse(seq_file, "fasta"):
        seq = str(record.seq).upper().encode()
        hash_object = hashlib.md5(seq)
        hash_map[hash_object.hexdigest()] = record.id
        seq_hash[str(record.seq)] = record.id
    return hash_map,seq_hash

def get_set_names(designation_csv):
    designation_dict = {}
    with open(designation_csv,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            designation_dict[row["taxon"]] = row["set_name"]
    return designation_dict

def get_hash_string(record):
    seq = str(record.seq).upper().encode()
    hash_object = hashlib.md5(seq)
    hash_string = hash_object.hexdigest()
    return hash_string

def get_dict(in_csv,name_column,data_column):
    this_dict = {}
    with open(in_csv,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            this_dict[row[name_column]] = row[data_column]
    return this_dict