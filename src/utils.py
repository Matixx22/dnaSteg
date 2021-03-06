from textwrap import wrap
import os
import re

char_to_dna = {
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

dna_to_char = {v: k for k, v in char_to_dna.items()}

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


def hide(msg, out_file):
    print(f'Hiding "{msg}" in sequence...')

    encoded_msg = to_dna(msg)
    encoded_msg_str = ''.join(encoded_msg)
    base_file = ''

    # choose base dna file based on length of encoded message
    all_bases = re.findall('[0-9]+', ''.join(os.listdir('../res')))
    all_bases = [int(x) for x in all_bases]
    all_bases.sort()

    for base in all_bases:
        if base > len(encoded_msg_str):
            base_file = '../res/base' + str(base) + '.dna'
            break

    try:
        with open(base_file, 'r') as in_file:
            sequence = in_file.read()

    except IOError as e:
        print(e)
        exit(1)

    # converting dna to binary
    enc_bin = dna_to_bin(encoded_msg)

    s = wrap(sequence, 3)
    base_bin = dna_to_bin(s)

    # xoring message with base
    xor = xor_bin(enc_bin, base_bin)

    # converting binary to dna
    dna = bin_to_dna(xor)
    print('Hidden message :', dna)

    with open(out_file, 'w') as out:
        out.write(dna)

    print('Success')


def extract(hid_file):
    # extracting

    # read hidden
    with open(hid_file, 'r') as h:
        hidden_message = h.read()

    # Open and read base dna file with length equal the hidden_message length
    try:
        with open('../res/base' + str(len(hidden_message)) + '.dna', 'r') as b:
            base = b.read()

    except IOError as e:
        print(e)
        exit(1)

    # decode from dna to binary
    hidden_message_bin = dna_to_bin(hidden_message)
    base_bin = dna_to_bin(base)

    # extract message
    decoded = xor_bin(hidden_message_bin, base_bin)

    decoded = bin(int(decoded, 2))[2:]

    # binary padding
    if (len(decoded) % 2) != 0:
        decoded = '0' + decoded

    decoded_dna = bin_to_dna(decoded)

    # dna padding
    if (len(decoded_dna) % 3) != 0:
        decoded_dna = 'A' * (3 - len(decoded_dna) % 3) + decoded_dna

    decoded_dna = wrap(decoded_dna, 3)

    # decode from dna to text
    decoded_message = ''.join(from_dna(decoded_dna))

    # print decoded_message
    print('Extracted hidden message:', decoded_message)


def to_dna(msg):
    encoded_message = [char_to_dna[letter] for letter in msg]

    return encoded_message


def from_dna(dna):
    decoded_message = [dna_to_char[chunk] for chunk in dna]

    return decoded_message


def dna_to_bin(seq):
    seq_base4 = []
    seq_bin = []
    bin_seq_len = 6 * len(seq)

    for char in seq:
        seq_base4.append(''.join([dna_to_num[letter] for letter in char]))

    for num in seq_base4:
        digit_list = []
        for digit in num:
            digit_list.append('{:0>2b}'.format(int(digit)))

        seq_bin.append(''.join(digit_list))

    seq_bin_str = ('{:0>' + str(bin_seq_len) + 'b}').format(int(''.join(seq_bin), 2))

    return seq_bin_str


def bin_to_dna(binary):
    result_list = []

    bin_str_list = wrap(binary, 6)

    for i in range(len(bin_str_list)):
        one_letter_bin = wrap(bin_str_list[i], 2)

        for b in one_letter_bin:
            result_list.append(int(b, 2))

    dna = ''.join([num_to_dna[num] for num in result_list])

    return dna


def xor_bin(msg, base):
    xor_result = int(msg, 2) ^ int(base, 2)
    xor_result = ('{:0>' + str(len(base)) + 'b}').format(xor_result)

    return xor_result
