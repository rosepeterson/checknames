# checknames
##### Software required: python 3 and biopython

## Check if tip labels in your phylogeny match the taxa in your fasta alignment:
##### phylogeny format: newick, nexus, nexml, phyloxml, or cdao

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick </code></pre>

## Prune the alignment of taxa that are **NOT** in your phylogeny:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -r True -g out.fasta  </code></pre>

## Prune the phylogeny for taxa that are **NOT** in your alignment:
##### output phylogeny format will be the same as the input phylogeny format

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick-u True -ot out.tree  </code></pre>

## Prune both phylogeny **AND** alignment:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -u True -ot out.tree -r True -g out.fasta  </code></pre>


