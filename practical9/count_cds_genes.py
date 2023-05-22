stop_codon = input()

output_file_name = stop_codon + "_stop_genes.fa"

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, \
     open(output_file_name, 'w') as outfile:

    gene_name = ""
    sequence = ""

    coding_seq_counter = 0

    for line in infile:
        if line.startswith('>'):
            if sequence != "" and sequence.endswith(stop_codon):
                outfile.write(">" + gene_name + "_" + str(coding_seq_counter) + "\n")
                outfile.write(sequence + "\n")
                sequence = ""
                coding_seq_counter = 0
            gene_name = line.strip()[1:]
            sequence = ""
        else:
            sequence += line.strip()
            if line.strip().endswith(stop_codon):
                coding_seq_counter += 1
    if sequence != "" and sequence.endswith(stop_codon):
        outfile.write(">" + gene_name + "_" + str(coding_seq_counter) + "\n")
        outfile.write(sequence + "\n")