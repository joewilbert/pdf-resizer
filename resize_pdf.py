import sys
import os
import PyPDF2

def resize_pdf(input_file):
    WID = 612
    HEI = 792

    try:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        for page_number in range(len(reader.pages)):
            pdfpage = reader.pages[page_number]
            pdfpage.scale_to(width=WID, height=HEI)
            writer.add_page(pdfpage)

        output_file = os.path.join(os.path.dirname(input_file), os.path.splitext(os.path.basename(input_file))[0] + "_resized.pdf")
        with open(output_file, 'wb') as outputStream:
            writer.write(outputStream)

        print(f"Resized PDF saved as: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except PyPDF2.utils.PdfReadError:
        print(f"Invalid PDF file: {input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_resizer.py <input_file>")
        sys.exit(1)

    input_file = os.path.abspath(sys.argv[1])
    resize_pdf(input_file)