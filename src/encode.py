from textwrap import wrap

code = {
    'a': 'AAA', 'b': 'AAC', 'c': 'AAG', 'd': 'AAT',
    'e': 'ACA', 'f': 'ACC', 'g': 'ACG', 'h': 'ACT',
    'i': 'AGA', 'j': 'AGC', 'k': 'AGG', 'l': 'AGT',
    'm': 'ATA', 'n': 'ATC', 'o': 'ATG', 'p': 'ATT',
    'q': 'CAA', 'r': 'CAC', 's': 'CAG', 't': 'CAT',
    'u': 'CCA', 'v': 'CCC', 'w': 'CCG', 'x': 'CCT',
    'y': 'CGA', 'z': 'CGC', 'A': 'CGG', 'B': 'CGT',
    'C': 'CTA', 'D': 'CTC', 'E': 'CTG', 'F': 'CTT',
    'G': 'GAA', 'H': 'GAC', 'I': 'GAG', 'J': 'GAT',
    'K': 'GCA', 'L': 'GCC', 'M': 'GCG', 'N': 'GCT',
    'O': 'GGA', 'P': 'GGC', 'Q': 'GGG', 'R': 'GGT',
    'S': 'GTA', 'T': 'GTC', 'U': 'GTG', 'V': 'GTT',
    'W': 'TAA', 'X': 'TAC', 'Y': 'TAG', 'Z': 'TAT',
    '1': 'TCA', '2': 'TCC', '3': 'TCG', '4': 'TCT',
    '5': 'TGA', '6': 'TGC', '7': 'TGG', '8': 'TGT',
    '9': 'TTA', '0': 'TTC', ' ': 'TTG', '.': 'TTT'
}

dna_to_num = {
    'A': '0',
    'C': '1',
    'G': '2',
    'T': '3'
}

num_to_dna = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}


def hide(msg, dna_file, out_file):
    print(f'Hiding "{msg}" in sequence in {dna_file}...')

    with open(dna_file, 'r') as in_file:
        sequence = in_file.read()

    # TODO: Do magic:
    #  1. encode message to DNA sequence - DONE
    #  2. think about a technique how to hide encoded message in a DNA sequence - probably xor would be ok - DONE
    #  3. do a message extraction from encoded DNA file

    encoded_msg = encode(msg)
    # print(encoded_msg)
    # print(wrap(sequence, 3))

    enc_base4 = []
    base_base4 = []

    for char in encoded_msg:
        # print(''.join([nucleotides_map[letter] for letter in char]), end=' ')
        enc_base4.append(''.join([dna_to_num[letter] for letter in char]))

    s = wrap(sequence, 3)
    # print('')
    # print('==============================')

    for char in s:
        # print(''.join([nucleotides_map[letter] for letter in char]), end=', ')
        base_base4.append(''.join([dna_to_num[letter] for letter in char]))

    # print(enc_base4)
    # print(base_base4)

    num_list = []
    base_list = []

    for num in enc_base4:
        digit_list = []
        for digit in num:
            digit_list.append('{:0>2b}'.format(int(digit)))
            # print('{:0>2b}'.format(int(digit)))
        # print('')
        num_list.append(''.join(digit_list))

    for num in base_base4:
        digit_list = []
        for digit in num:
            digit_list.append('{:0>2b}'.format(int(digit)))
            # print('{:0>2b}'.format(int(digit)))
        # print('')
        base_list.append(''.join(digit_list))

    # print(num_list)
    # print(base_list)

    # Message
    msg_length = 6 * len(num_list)
    msg_bin = ('{:0>'+str(msg_length)+'b}').format(int(''.join(num_list), 2))
    # print('      '+msg_bin)

    # Base
    base_len = 6 * len(base_list)
    base_bin = ('{:0>'+str(base_len)+'b}').format(int(''.join(base_list), 2))
    # print(base_bin)

    # XOR

    encoded_bin = int(msg_bin, 2) ^ int(base_bin, 2)
    encoded_bin = ('{:0>'+str(base_len)+'b}').format(encoded_bin)
    # print(encoded_bin)
    #
    enc_list = wrap(encoded_bin, 6)
    # print(enc_list)
    #

    decoded = []
    for i in range(len(enc_list)):
        decoded.append(bin_to_dna(enc_list[i]))

    # Fully hidden string in dna
    print(''.join(decoded))

    print('')

    # TODO: Extracting

    # with open(out_file, 'w') as out:
    #     hidden = sequence + msg
    #     print(hidden)
    #     out.write(hidden)

    print('Success')


def encode(msg):
    encoded_message = [code[letter] for letter in msg]
    # print(encoded_message)
    return encoded_message


def dna_to_bin(seq):
    seq_base4 = []

    for char in seq:
        seq_base4.append(''.join([dna_to_num[letter] for letter in char]))


def bin_to_dna(binary):
    result_list = []

    letters_bin = wrap(binary, 2)

    for b in letters_bin:
        result_list.append(int(b, 2))

    result = ''.join([num_to_dna[num] for num in result_list])

    return result
