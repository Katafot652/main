def combine_sequences(seq1, seq2):
    result = []
    for x, y in zip(seq1, seq2):
        result.append(x)
        result.append(y)
    return result


seq1 = input().split()
seq2 = input().split()

combined = combine_sequences(seq1, seq2)
print(" ".join(combined))
