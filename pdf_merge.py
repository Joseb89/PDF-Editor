import tkinter
import os
import pdf

from pypdf import PdfWriter

def main():
    try:
        root = tkinter.Tk()
        root.withdraw()

        merger = PdfWriter()

        file_path, continue_merge = ""

        while continue_merge != "N":
            file_path = pdf.open_pdf_file()
            
            merger.append(file_path)

            continue_merge = input("Do you wish to add more files? (Y/N)").upper()

        with open(os.path.dirname(file_path) + "\\\HillCountryHospice_11-11-2025.pdf", "wb") as new_file:
            merger.write(new_file)

    except FileNotFoundError:
        print("File not found.")        

if __name__ == "__main__":
    main()        