# checknames
##### Software required: python 3, biopython, and pandas

## Check if tip labels in a phylogeny match the headers in a fasta alignment:
##### Phylogeny format: newick, nexus, nexml, phyloxml, or cdao
##### Alignment file must be in fasta format

## Print mismatched labels between phylogeny and alignment

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick </code></pre>

## Prune taxa from the alignment that are **NOT** in the phylogeny:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -r True -g out.fasta  </code></pre>

## Prune taxa from the phylogeny that are **NOT** in the alignment:
<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -u True -ot out.tree  </code></pre>

## Prune both the phylogeny **AND** the alignment:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -u True -ot out.tree -r True -g out.fasta  </code></pre>

## Check if taxa names in a csv file match the tip labels in a phylogeny:
##### Phylogeny format: newick, nexus, nexml, phyloxml, or cdao
##### CSV file either T for tab separated or C for comma separated 

## Print mismatched labels between phylogeny and csv file
<pre><code> python matchcsv2tree.py -c example.csv -p example.tree -t newick -s C </code></pre> 

## Prune taxa from the CSV file that are **NOT** in the phylogeny:

<pre><code> python matchcsv2tree.py -c example.csv -p example.tree -t newick -s C -k True -oc out.csv </code></pre> 

## Prune taxa from the phylogeny that are **NOT** in the CSV file:

<pre><code> python matchcsv2tree.py -c example.csv -p example.tree -t newick -s C -u True -ot out.tree </code></pre> 

## Prune both the phylogeny **AND** the CSV file:

<pre><code> python matchcsv2tree.py -c example.csv -p example.tree -t newick -s C -u True -ot out.tree -k True -oc out.csv </code></pre> 


