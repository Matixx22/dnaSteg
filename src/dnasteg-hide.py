import argparse

from utils import hide


def main():
    parser = argparse.ArgumentParser(description="dnaSteg - hide a message in a DNA sequence")

    parser.add_argument('message', help='Message to hide')
    parser.add_argument('out', help='Output file')

    args = parser.parse_args()

    message = args.message
    out = args.out

    hide(message, out)


if __name__ == '__main__':
    main()
