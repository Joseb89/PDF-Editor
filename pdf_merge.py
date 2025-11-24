import tkinter
import os
import pdf

from pypdf import PdfWriter

root = tkinter.Tk()
root.withdraw()

file_path1 = pdf.open_pdf_file()

file_path2 = pdf.open_pdf_file()

merger = PdfWriter()

merger.append(file_path1)
merger.append(file_path2)

with open(os.path.dirname(file_path1) + "\\\HillCountryHospice_11-11-2025.pdf", "wb") as new_file:
    merger.write(new_file)