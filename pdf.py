from tkinter import filedialog

__directory = "C:\\Users\\acms\\Documents"

def open_pdf_file():
    return filedialog.askopenfilename(
    initialdir=__directory,
    title='Select File',
    filetypes=(("PDF Files", "*.pdf")))