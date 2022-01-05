# checknames
###Software required: python 3 and biopython

##If you simply want to check if tip labels in your phylogeny match the taxa in your fasta alignment:

python matchfasta2tree.py -f <yourfastaalignmet> -p <yourtreefile> -t <phylogeny format: newick, nexus, nexml, phyloxml, or cdao> 

##If you want to prune the alignment for taxa that are not in your phylogeny:

python matchfasta2tree.py -f <yourfastaalignmet> -p <yourtreefile> -t <phylogeny format: newick, nexus, nexml, phyloxml, or cdao> -r True -g <outputalignment>

##If you want to prune the phylogeny for taxa that are not in your alignment:

python matchfasta2tree.py -f <yourfastaalignmet> -p <yourtreefile> -t <phylogeny format: newick, nexus, nexml, phyloxml, or cdao> -u True -ot <outputtreefile>

##If you want to prune both phylogeny alignment:

python matchfasta2tree.py -f <yourfastaalignmet> -p <yourtreefile> -t <phylogeny format: newick, nexus, nexml, phyloxml, or cdao> -u True -ot <outputtreefilet> -r True -g <outputalignment>


