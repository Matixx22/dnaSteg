import argparse

from utils import extract


def main():
    parser = argparse.ArgumentParser(description="dnaSteg-extract - extract a message from a DNA sequence")

    parser.add_argument('file', help='File with hidden message in DNA')
    parser.add_argument('base', help='Base file with DNA sequence')

    args = parser.parse_args()

    file = args.file
    base = args.base

    extract(file, base)


if __name__ == '__main__':
    main()
