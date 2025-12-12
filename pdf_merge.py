import tkinter
import os
import pdf

from pypdf import PdfWriter

def main():
    try:
        root = tkinter.Tk()
        root.withdraw()

        merger = PdfWriter()

        file_path1 = pdf.open_pdf_file()
        file_path2 = pdf.open_pdf_file()
                
        merger.append(file_path1)
        merger.append(file_path2)

        while True:
            continue_merge = input("Do you wish to add another file to merge? (Y/N)").capitalize()

            if continue_merge == "N":
                break

            elif continue_merge == "Y":
                new_file = pdf.open_pdf_file()
                merger.append(new_file)

            else:
                print("Please enter a valid response.")

        saved_file_path = os.path.dirname(file_path1)       

        file_name = input("Please input file name: ")         

        with open(f"{saved_file_path}{"\\"}{file_name}{".pdf"}", "wb") as new_file:
            merger.write(new_file)

    except FileNotFoundError:
        print("File not found.")        

if __name__ == "__main__":
    main()        