import argparse

from utils import extract


def main():
    parser = argparse.ArgumentParser(description="dnaSteg-extract - extract a message from a DNA sequence")

    parser.add_argument('file', help='File with hidden message in DNA')

    args = parser.parse_args()

    file = args.file

    extract(file)


if __name__ == '__main__':
    main()
