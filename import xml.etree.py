import xml.etree.ElementTree as ET
import os

# Set your path for the file and test if it is correct
file_path = r"C:\Users\nurhu\Documents\raxml-ng_v1.2.0_linux_x86_64\input.xml"

if os.path.exists(file_path):
    print("File found!")
else:
    print("File not found. Check the path.")


# Input BEAST XML file
xml_file = "input.xml" 

# Output FASTA file
fasta_file = "output.fasta"

# Parse XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Open the FASTA file for writing
with open(fasta_file, "w") as fasta:
    # Find all sequence elements
    for seq in root.findall(".//sequence"):
        taxon = seq.get("taxon")  # Extract taxon name
        sequence = seq.get("value")  # Extract sequence data
        if taxon and sequence:
            fasta.write(f">{taxon}\n{sequence}\n")

print("FASTA extraction complete. Check 'output.fasta'.")


