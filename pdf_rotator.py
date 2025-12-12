import os
import shutil
import pdf

import tkinter

from pypdf import PdfReader, PdfWriter

def main():
    root = tkinter.Tk()
    root.withdraw()

    try:
        file_path = pdf.open_pdf_file()

        reader = PdfReader(file_path)

        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(-90)

            writer.add_page(page)

        saved_file = os.path.basename(file_path)

        with open(saved_file, "wb") as new_file:
            writer.write(new_file)

        os.remove(file_path)

        shutil.move(saved_file, os.path.dirname(file_path))
        
    except FileNotFoundError:
        print('File not found.')

if __name__ == "__main__":
    main()      