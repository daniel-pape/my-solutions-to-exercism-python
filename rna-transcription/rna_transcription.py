def to_rna(dna_strand: str):
    def validate_input():
        def is_input_valid():
            checks = [nucleotide in 'GCTA' for nucleotide in dna_strand]

            return all(checks)

        if not is_input_valid():
            msg = 'Function `to_rna(dna_strand)` requires string ' \
                  '`dna_strand` to only contain letters from `GCTA`. ' \
                  'But instead `dna_strand={}`.'.format(dna_strand)

            raise Exception(msg)

    validate_input()
    t = str.maketrans('GCTA', 'CGAU')

    return dna_strand.translate(t)
