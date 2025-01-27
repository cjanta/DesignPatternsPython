# pip install pypdf2

from PyPDF2 import PdfMerger

# List of PDF files to merge
pdf_files = [
    r"pdf_tools\pdfkit\Bewerbung_Lebenslauf_svk.pdf", # 0
    r"pdf_tools\pdf_merge\to_merge\5_GIS-Rodias_Zeugnis.pdf", # 0 
]



# Output file name
output_file = r"pdf_tools\pdf_merge\to_merge\Bewerbung_svk.pdf"

merger = PdfMerger()

index = 0
for pdf in pdf_files:
    merger.append(pdf)
    index += 1


merger.write(output_file)
merger.close()

print(f"Merged PDF saved as: {output_file}")

pdf_files_history = [
    r"pdf_tools\pdf_merge\to_merge\4_Albers_Zeugnis.pdf", #
    r"pdf_tools\pdf_merge\to_merge\3_Metro_Zeugniss.pdf", #  //nur erste Seite vom scan
    r"pdf_tools\pdf_merge\to_merge\2_Arnold_Zeugnis.pdf", #  //nur erste Seite vom Scan
    r"pdf_tools\pdf_merge\to_merge\1_Berufsschule_Zimmermann_Zeugnis.pdf",
    r"pdf_tools\pdf_merge\to_merge\0_Realschule_Zeugnis.pdf",
    
]
merger = PdfMerger()
history_file = r"pdf_tools\pdf_merge\to_merge\Zeugnisse_historie_svk.pdf"
index = 0
for pdf in pdf_files_history:
    if index == 1 or index == 2 :
         merger.append(pdf, pages=(0, 1))
    else :
         merger.append(pdf)
    index += 1


merger.write(history_file)
merger.close()

print(f"Merged PDF saved as: {history_file}")