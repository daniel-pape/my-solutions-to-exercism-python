def distance(strand_a, strand_b):
    len_a = len(strand_a)
    len_b = len(strand_b)
    lengths_match = (len_a == len_b)

    if not lengths_match:
        raise ValueError('Strands have different lengths.')

    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
