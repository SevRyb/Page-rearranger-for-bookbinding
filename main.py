from PyPDF2 import PdfFileWriter, PdfFileReader
import sys, os


def main(filepath):

    output_pdf = PdfFileWriter()
    output_pdf_side_A = PdfFileWriter()
    output_pdf_side_B = PdfFileWriter()

    # In values
    n_blocks = int(input("[?] Number of blocks: "))
    n_sheets_in_block = int(input("[?] Number of sheets in block: "))

    read_file = open(filepath, 'rb')
    input_pdf = PdfFileReader(read_file)
    
    total_pages = input_pdf.getNumPages()
    print("[INFO] Total pages:", total_pages)

    pages_out_of_block = total_pages - (n_blocks * n_sheets_in_block * 4)
    sheets_in_last_block = n_sheets_in_block + int(pages_out_of_block / 4)

    if pages_out_of_block != 0:
        print("[INFO] There is one outsized block")
        print("[INFO] Number of sheets in last block:", sheets_in_last_block)

    page_offset = 0
    for block in range(n_blocks):

        if block == n_blocks - 1:
            n_sheets_in_block = sheets_in_last_block

        page_A0 = page_offset + 1
        page_A1 = page_offset + (n_sheets_in_block * 4 - 2)
        page_B0 = page_offset + (n_sheets_in_block * 4 - 1)
        page_B1 = page_offset

        for sheet in range(n_sheets_in_block):
            # One file
            output_pdf.addPage(input_pdf.getPage(page_A0))
            output_pdf.addPage(input_pdf.getPage(page_A1))
            output_pdf.addPage(input_pdf.getPage(page_B0))
            output_pdf.addPage(input_pdf.getPage(page_B1))
            # Side A & B (separate files)
            output_pdf_side_A.addPage(input_pdf.getPage(page_A0))
            output_pdf_side_A.addPage(input_pdf.getPage(page_A1))
            output_pdf_side_B.addPage(input_pdf.getPage(page_B0))
            output_pdf_side_B.addPage(input_pdf.getPage(page_B1))

            page_A0 += 2
            page_A1 -= 2
            page_B0 -= 2
            page_B1 += 2

        page_offset += n_sheets_in_block * 4

    f = os.path.join(
        os.path.dirname(filepath) + "/out/", 
        os.path.basename(os.path.splitext(filepath)[0]))

    write_file = open(f + " (side_by_side).pdf", 'wb')
    output_pdf.write(write_file)
    write_file.close()
    read_file.close()

    side_A_file = open(f + " (side_A).pdf", 'wb')
    output_pdf_side_A.write(side_A_file)
    side_A_file.close()

    side_B_file = open(f + " (side_B).pdf", 'wb')
    output_pdf_side_B.write(side_B_file)
    side_B_file.close()


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("[INFO] Usage:")
        print("python booklet.py path/to/PDF/file\n")
        main(input("[?] Path to input PDF file: "))
    else:
        main(sys.argv[1])

