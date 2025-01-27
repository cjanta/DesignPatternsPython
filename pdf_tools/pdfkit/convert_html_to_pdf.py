import pdfkit
import os
# pip install pdfkit
# os install wkhtmltopdf.exe
# pdfkit.from_url('http://google.com', 'out.pdf')

path = r"pdf_tools\pdfkit\lebenslauf.html"
out_path_filename = r"pdf_tools\pdfkit\Bewerbung_Lebenslauf_svk.pdf"


config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options = {
    'enable-local-file-access': None,  # Allow access to local files
}


pdfkit.from_file(path, out_path_filename, configuration=config, options=options)
