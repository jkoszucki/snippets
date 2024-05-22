# snippets for bioinformatics
# Maniac Output Description

Maniac output files are written in the user-defined output directory. The ANI results and associated metrics are found in the file `genome-alignment.csv`. This file is a table with various metrics summarized in the table below:

| Metrics        | Description                                                                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ANI**        | Average nucleotide identity between the query and reference sequences                                                                                                               |
| **len_1**      | The length of the query sequence                                                                                                                                                    |
| **len_2**      | The length of the reference sequence                                                                                                                                                |
| **ani_alnlen** | The total length of aligned nucleotides between the query and reference sequences                                                                                                    |
| **af_1**       | Alignment fraction of the query sequence calculated by dividing the aligned length by the total length of the query sequence                                                                                      |
| **af_2**       | Alignment fraction of the reference sequence calculated by dividing the aligned length by the total length of the reference sequence                                                                                  |
| **af_min**     | The minimum alignment fraction between the query and reference sequence calculated by dividing the aligned nucleotide length by the shorter sequence between the query and reference sequence                 |
| **af_max**     | The maximum alignment fraction between the query and reference sequence calculated by dividing the aligned nucleotide length by the longer sequence between the query and reference sequence                   |
| **af_mean**    | Mean alignment fraction between the query and reference sequences. It is calculated by averaging the alignment fraction of both query and reference sequences weighted by their length. Users can also calculate `af_mean` by considering the alignment fraction between pairs since the results of MANIAC are asymmetrical i.e (af_1 + af_2)/2                                                                                                                                 |
| **af_jaccard** | The jaccard index of the alignment fraction calculated as the ratio of the aligned length to the total length of the union of the query and reference sequences                                                              |
| **seq1_n_prots** | Number of proteins or CDS in the query sequence                                                                                                                                    |
| **seq2_n_prots** | Number of proteins or CDS in the reference sequence                                                                                                                                 |
| **min_prots**    | The minimum number of proteins or CDS between the query and reference sequences                                                                                                     |
| **wGRR**         | wGRR is the weighted gene repertoire relatedness. It is calculated as the ratio of bi-directional best hits between the query and reference genomes weighted by the sequence identity of homologs (CDS or protein homologs for the CDS or protein mode respectively) |
