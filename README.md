# pdf-combine

`pdf-combine` is a Python command-line tool designed for merging multiple pages of a PDF into a single page.This is also called 'n-up'. This is particularly useful for printing purposes, where you might want to fit multiple pages onto one sheet of paper.

## Usage

```bash
pdf-combine input.pdf output.pdf [-l] [-n LAYOUT]
```

### Arguments:

- `input.pdf`: Path to the input PDF file
- `output.pdf`: Path where the output PDF file will be saved

### Options:

- `-l, --landscape`: Use landscape mode instead of portrait mode
- `-n LAYOUT, --layout LAYOUT`: Layout of the pages (e.g., 2x2, 3x4). Default is "1x2"

## Examples:

1. Basic usage (default 1x2 layout in portrait mode):
   ```bash
   pdf-combine input.pdf output.pdf
   ```

2. Using landscape mode:
   ```bash
   pdf-combine input.pdf output.pdf -l
   ```

3. Custom layout (2x2 in portrait mode):
   ```bash
   pdf-combine input.pdf output.pdf -n 2x2
   ```

4. Custom layout in landscape mode:
   ```bash
   pdf-combine input.pdf output.pdf -l -n 2x4
   ```

Note: The layout should be specified as "NxM" where N and M are positive integers representing the number of rows and columns respectively.
