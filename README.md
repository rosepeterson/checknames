# checknames
##### Software required: python 3 and biopython

## Check if tip labels in your phylogeny match the headers in your fasta alignment:
##### phylogeny format: newick, nexus, nexml, phyloxml, or cdao
##### alignment file must be in fasta format

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick </code></pre>

## Prune taxa from the alignment that are **NOT** in your phylogeny:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -r True -g out.fasta  </code></pre>

## Prune taxa from the phylogeny that are **NOT** in your alignment:
##### output phylogeny format will be the same as the input phylogeny format

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick-u True -ot out.tree  </code></pre>

## Prune both phylogeny **AND** alignment:

<pre><code> python matchfasta2tree.py -f example.fasta -p example.tree -t newick -u True -ot out.tree -r True -g out.fasta  </code></pre>


