# pip install markdown-pdf
# python -m venv .\.venv
# .venv\Scripts\activate
from markdown_pdf import Section, MarkdownPdf

path_filename = "IHK-AP1.md"

# Read content from the Markdown file
with open(path_filename, "r", encoding="utf-8") as file:
    markdown_content = file.read()

pdf = MarkdownPdf()

# Add the entire content as a single section
pdf.add_section(Section(markdown_content))

# Save the PDF
pdf.save("IHK-AP1.pdf")

print("PDF has been created", path_filename)
