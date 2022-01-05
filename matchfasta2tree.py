#!/usr/bin/env python

import re
from sys import argv
import argparse


from Bio import SeqIO
from Bio import Phylo


parser = argparse.ArgumentParser(description="Written under python 3 and requires Biopython and dendropy. ")
parser.add_argument('-f', '--fasta' , dest = 'fasta' , type = str , default= None , required= True, help = 'Fasta alignment to compare')
parser.add_argument('-p', '--phylo', dest = 'phylo', type = str, default = None, required = True, help = 'phylogeny')
parser.add_argument('-t', '--filetype', dest = 'filetype', type = str, default = None, required = True, help = 'phylogeny format: newick, nexus, nexml, phyloxml, or cdao')
parser.add_argument('-u', '--prunetree', dest = 'prunetree', type = str, default = None, required = False, help = 'True or False for pruning non-matching tips from phylogeny')
parser.add_argument('-ot', '--outtree', dest = 'outtree', type = str, default = None, required = False, help = 'pruned phylogeny output file')
parser.add_argument('-r', '--prunealign', dest = 'prunealign', type = str, default = None, required = False, help = 'True or False for pruning non-matching tips from alignment')
parser.add_argument('-g', '--outalign', dest = 'outalign', type = str, default = None, required = False, help = 'pruned alignemment file')


args, unknown = parser.parse_known_args()


def non_match_elements(list1, list2):
    non_match = []
    for i in list1:
        if i not in list2:
            non_match.append(i)
    return non_match


list1 = []
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	list1.append(seq_record.id)


trees = Phylo.read(args.phylo, args.filetype)
list2 = [term.name for term in trees.get_terminals()]

	
non_match = non_match_elements(list1,list2)
print("Names not found in phylogeny", non_match)


non_matchr = non_match_elements(list2,list1)
print("Names not found in alignment", non_matchr)

if args.prunetree == 'True':
	for x in non_matchr:
		trees.prune(x)
	with open(args.outtree, 'w') as handle:
		Phylo.write(trees, handle, "newick")

if args.prunealign == 'True':
	record_dict = SeqIO.to_dict(SeqIO.parse(args.fasta, "fasta"))
	for x in non_match:
		del record_dict[x]
	with open(args.outalign, 'w') as handle:
    	SeqIO.write(record_dict.values(), handle, 'fasta')

	
	

	

