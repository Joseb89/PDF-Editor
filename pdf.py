from tkinter import filedialog

def open_pdf_file():
    return filedialog.askopenfilename(
    initialdir="C:\\Users\\acms\\Documents",
    title='Select File',
    filetypes=(("PDF Files", "*.pdf"),))