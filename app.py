import os
import shutil
import pdf
import config

import tkinter

from pypdf import PdfReader, PdfWriter
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/rotate_pdf", methods=["GET", "POST"])
def rotate_pdf():
    if request.method == "POST":
        file = request.files["pdf_file"]

        reader = PdfReader(file)

        writer = PdfWriter()

        angle = int(request.form['angle'])

        for page in reader.pages:
            page.rotate(angle)

            writer.add_page(page)

        saved_file = os.path.basename(file.filename)

        with open(saved_file, "wb") as new_file:
            writer.write(new_file)   

        shutil.move(saved_file, config.file_path + file.filename)

    return render_template("pdf_rotate.html")

@app.route("/merge_pdf", methods=["POST"])
def merge_pdf():
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

if __name__ == '__main__':
    app.run(debug=True)        