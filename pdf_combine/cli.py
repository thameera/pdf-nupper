import argparse
import re
from .core import combine

def validate_layout(layout):
    if not re.match(r'^\d+x\d+$', layout):
        raise argparse.ArgumentTypeError("Layout must be in the format 'XxY' where X and Y are positive integers.")
    return layout

def main():
    parser = argparse.ArgumentParser(description="N-up PDF pages")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("output_pdf", help="Output PDF file")
    parser.add_argument("-l", "--landscape", action="store_true", help="Use landscape mode instead of portrait mode")
    parser.add_argument("-n", "--layout", type=validate_layout, default="1x2", help="Layout of the pages")

    args = parser.parse_args()

    rows, cols = map(int, args.layout.split("x"))

    combine(args.input_pdf, args.output_pdf, args.landscape, rows, cols)

if __name__ == "__main__":
    main()
