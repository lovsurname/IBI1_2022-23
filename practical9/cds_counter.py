seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
codons = ['ATG', 'TAA', 'TGA']
count = 0
for i in range(len(seq)):
    if seq[i:i+3] == codons[0]:
        for j in range(i+3, len(seq)):
            if seq[j:j+3] == codons[1] or seq[j:j+3] == codons[2]:
                count += 1
    break
print("Total number of possible coding sequences in the sequence: ", count)