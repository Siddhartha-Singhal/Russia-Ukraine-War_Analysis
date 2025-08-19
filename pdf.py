import nbconvert
import nbformat

# Load your notebook
notebook_filename = "code.ipynb"
with open(notebook_filename) as f:
    notebook = nbformat.read(f, as_version=4)

# Convert to PDF
pdf_exporter = nbconvert.PDFExporter()
pdf_exporter.exclude_output_prompt = True  # Optional: removes "In []:" prompts

(body, resources) = pdf_exporter.from_notebook_node(notebook)

# Write to PDF file
output_filename = "code_report.pdf"
with open(output_filename, "wb") as f:
    f.write(body)

print(f"Notebook converted successfully: {output_filename}")
