from pypdf import PdfWriter, PdfReader
from pypdf.generic import RectangleObject

A4_WIDTH = 595.28  # A4 width in points
A4_HEIGHT = 841.89  # A4 height in points

def combine(input_pdf_path, output_pdf_path, is_landscape=False, rows=1, cols=2):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    num_pages = len(reader.pages)
    if is_landscape:
        width = A4_HEIGHT
        height = A4_WIDTH
    else:
        width = A4_WIDTH
        height = A4_HEIGHT

    for i in range(0, num_pages, rows*cols):
        new_page = writer.add_blank_page(width=width, height=height)

        page_width = width / cols
        page_height = height / rows

        positions = [(col * page_width, (rows - 1 - row) * page_height) for row in range(rows) for col in range(cols)]

        for j in range(rows*cols):
            if i + j < num_pages:
                page = reader.pages[i + j]

                # Calculate the scale factor to maintain aspect ratio
                scale_x = page_width / page.mediabox.width
                scale_y = page_height / page.mediabox.height
                scale = min(scale_x, scale_y)  # Use the smaller scale to ensure it fits

                page.scale_by(scale)

                # Adjust the positions to center the page horizontally and vertically
                x_offset = (page_width - page.mediabox.width) / 2
                y_offset = (page_height - page.mediabox.height) / 2

                # Translate the page to the correct position
                position = positions[j]
                translation_matrix = [1, 0, 0, 1, position[0] + x_offset, position[1] + y_offset]
                page.mediabox = RectangleObject([0, 0, page_width, page_height])
                new_page.merge_transformed_page(page, translation_matrix)

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)
