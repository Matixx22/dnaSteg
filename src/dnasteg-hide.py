import argparse

from utils import hide


def main():
    parser = argparse.ArgumentParser(description="dnaSteg - hide a message in a DNA sequence")

    parser.add_argument('message', help='Message to hide')
    parser.add_argument('file', help='Base file with DNA sequence')
    parser.add_argument('out', help='Output file with hidden message')

    args = parser.parse_args()

    message = args.message
    file = args.file
    out = args.out

    hide(message, file, out)


if __name__ == '__main__':
    main()
