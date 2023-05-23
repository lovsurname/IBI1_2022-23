def dna_coding(sequence):
    sequence = sequence.upper()
    start = sequence.find('ATG')
    stop = sequence.find('TGA')
    coding = sequence[start:stop + 3]
    coding_percentage = len(coding) / len(sequence) * 100
    if coding_percentage > 50:
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 10:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'


print(dna_coding('atggtaagtcctggactACGTTAGCTGATTCAGTTGATTAGGATAA'))