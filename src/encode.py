def hide(msg, dna_file, out_file):
    print(f'Hiding "{msg}" in sequence in {dna_file}...')

    with open(dna_file, 'r') as in_file:
        sequence = in_file.read()

    # TODO: Do magic:
    #  1. encode message to DNA sequence
    #  2. think about a technique how to hide encoded message in a DNA sequence

    with open(out_file, 'w') as out:
        hidden = sequence + msg
        print(hidden)
        out.write(hidden)

    print('Success')
