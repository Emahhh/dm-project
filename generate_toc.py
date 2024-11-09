"""
This script generates a Table of Contents (TOC) for every Jupyter notebook in the current folder.
The TOC is generated based on the markdown headers in the notebook.
"""

import nbformat
import os

def generate_toc(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)
    
    toc = "# Table of Contents\n\n"
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            for line in lines:
                if line.startswith('#'):
                    if any(line.strip() == '# Table of Contents' for line in lines):
                        continue
                    level = line.count('#')
                    header = line.strip('#').strip()
                    link = header.lower().replace(' ', '-').replace('`', '')
                    toc += f"{'  ' * (level - 1)}- [{header}](#{link})\n"
    
    # Create a new markdown cell with the TOC
    toc_cell = nbformat.v4.new_markdown_cell(toc)
    
    # Check if the first cell is a TOC cell and replace it if it is
    if nb.cells and nb.cells[0].cell_type == 'markdown' and nb.cells[0].source.startswith('# Table of Contents'):
        nb.cells[0] = toc_cell
    else:
        # Insert the TOC cell at the beginning of the notebook
        nb.cells.insert(0, toc_cell)
    
    # Write the modified notebook back to the file
    with open(notebook_path, 'w') as f:
        nbformat.write(nb, f)

# Find every .ipynb file in the current folder
notebook_dir = os.getcwd()
for file in os.listdir(notebook_dir):
    if file.endswith('.ipynb'):
        notebook_path = os.path.join(notebook_dir, file)
        generate_toc(notebook_path)
        print(f"TOC added to {notebook_path}")
