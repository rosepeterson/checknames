#!/usr/bin/env python

import re
from sys import argv
import argparse


from Bio import SeqIO
from Bio import Phylo
import pandas as pd

parser = argparse.ArgumentParser(description="Written under python 3 and requires Biopython and pandas")
parser.add_argument('-p', '--phylo', dest = 'phylo', type = str, default = None, required = True, help = 'Input phylogeny')
parser.add_argument('-c', '--csv', dest = 'csv', type = str, default = None, required = True, help = 'Input CSV file')
parser.add_argument('-t', '--filetype', dest = 'filetype', type = str, default = None, required = True, help = 'phylogeny format: newick, nexus, nexml, phyloxml, or cdao')
parser.add_argument('-s', '--sep', dest = 'csvsep', type = str, default = None, required = True, help = 'CSV separator: T for tab or C for comma')
parser.add_argument('-u', '--prunetree', dest = 'prunetree', type = str, default = None, required = False, help = 'True flag prunes non-matching taxa from phylogeny')
parser.add_argument('-ot', '--outtree', dest = 'outtree', type = str, default = None, required = False, help = 'output file for pruned phylogeny')
parser.add_argument('-k', '--prunecsv', dest = 'prunecsv', type = str, default = None, required = False, help = 'True flag prunes non-matching taxa from csv')
parser.add_argument('-oc', '--outcsv', dest = 'outcsv', type = str, default = None, required = False, help = 'output file name for pruned csv')


args, unknown = parser.parse_known_args()

def mismatch(list1, list2):
    nomatch = []
    for i in list1:
        if i not in list2:
            nomatch.append(i)
    return nomatch


trees = Phylo.read(args.phylo, args.filetype)
list1 = [term.name for term in trees.get_terminals()]

if args.csvsep == "T":
	df = pd.read_csv(args.csv, sep="	", header=0)

if args.csvsep == "C":
	df = pd.read_csv(args.csv, sep=",", header=0)

matrix2 = df[df.columns[0]].to_numpy()
list2 = matrix2.tolist()


non_match = mismatch(list1,list2)
print("Names not found in csv", "\n", non_match)

non_matchr = mismatch(list2,list1)
print("Names not found in phylogeny", "\n", non_matchr)

if args.prunetree == 'True':
	for x in non_match:
		trees.prune(x)
	with open(args.outtree, 'w') as handle:
		Phylo.write(trees, handle, "newick")

if args.prunecsv == 'True':
	
	dfindex =df.set_index(df.columns[0])
	
	dfindex = dfindex.drop(non_matchr)
	dfindex.to_csv(args.outcsv, index=True)






