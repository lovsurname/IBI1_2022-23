with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as infile, \
        open('TGA_genes.fa', 'w') as outfile:
    gene_name = ''
    gene_seq = ''

    # Loop through the input file
    for line in infile:
        if line.startswith('>'):
            if gene_seq.endswith('TGA'):
                # Write the gene sequence to the output file
                outfile.write('>%s\n%s\n' % (gene_name, gene_seq))

            # Store the new gene name and reset the sequence
            gene_name = line.strip().lstrip('>').split()[0]
            gene_seq = ''

        else:  # A line with sequence data
            gene_seq += line.strip()

    if gene_seq.endswith('TGA'):
        outfile.write('>%s\n%s\n' % (gene_name, gene_seq))