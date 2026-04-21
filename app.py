import os
import shutil
import config

from pypdf import PdfReader, PdfWriter
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/rotate_pdf", methods=["GET", "POST"])
def rotate_pdf():
    if request.method == "POST":
        try:
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

        except FileNotFoundError as error:
            print(error)
        except PermissionError as error:
            print(error)    

    return render_template("pdf_rotate.html")

@app.route("/merge_pdf", methods=["GET", "POST"])
def merge_pdf():
    if request.method == "POST":
        try:
            merger = PdfWriter()

            files = request.files.getlist("pdf_file")

            for file in files:
                merger.append(file)    

            file_name = request.form["file_name"]        

            with open(f"{config.file_path}{"\\"}{file_name}{".pdf"}", "wb") as new_file:
                merger.write(new_file)

        except FileNotFoundError:
            print("File not found.")

    return render_template("pdf_merge.html")        

if __name__ == '__main__':
    app.run(debug=True)        