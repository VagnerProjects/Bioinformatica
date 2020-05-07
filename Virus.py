from Coronavirus import SarsCoV2
import colorama
from colorama import Fore
from Bio.Seq import Seq
import Bio.SeqIO as BIO
from Bio import AlignIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from Bio import Entrez
import mysql.connector
import os


print("\n")
print(Fore.GREEN)
print("==============================================================================================================")

print(Fore.RED)

Entrez.email = "sinxberserker@gmail.com" 

filename = "USA.txt" 

#Pega uma sequencia de nucleotideos do genbank e envia para um arquivo txt
with Entrez.efetch(db="nucleotide",id="MT252677",rettype="gb", retmode="text") as net_handle:
        with open("C:\\Users\\vagner_lima\\Documents\\Python\\"+filename, "w") as out_handle:
            out_handle.write(net_handle.read())

print("Parsing...")

#Envia para o arquivo os dados coletados
out_handle.write(net_handle.read())


print("==============================================================================================================")