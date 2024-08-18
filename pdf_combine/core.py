from pypdf import PdfWriter, PdfReader
from pypdf.generic import RectangleObject

A4_WIDTH = 595.28  # A4 width in points
A4_HEIGHT = 841.89  # A4 height in points

def combine(input_pdf_path, output_pdf_path, is_landscape=False):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    num_pages = len(reader.pages)
    if is_landscape:
        width = A4_HEIGHT
        height = A4_WIDTH
    else:
        width = A4_WIDTH
        height = A4_HEIGHT

    for i in range(0, num_pages, 2):
        new_page = writer.add_blank_page(width=width, height=height)

        positions = [
            (0, 0),  # Left side
            (width / 2, 0)  # Right side
        ]

        for j in range(2):
            if i + j < num_pages:
                page = reader.pages[i + j]
                page.scale_by(width / page.mediabox.width)

                # Translate the page to the correct position
                position = positions[j]
                translation_matrix = [1, 0, 0, 1, position[0], position[1]]
                page.mediabox = RectangleObject([0, 0, width / 2, height])
                new_page.merge_transformed_page(page, translation_matrix)

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)
