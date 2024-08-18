import argparse
from .core import combine

def main():
    parser = argparse.ArgumentParser(description="N-up PDF pages")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("output_pdf", help="Output PDF file")
    parser.add_argument("-l", "--landscape", action="store_true", help="Use landscape mode instead of portrait mode")


    args = parser.parse_args()

    combine(args.input_pdf, args.output_pdf, args.landscape)

if __name__ == "__main__":
    main()
