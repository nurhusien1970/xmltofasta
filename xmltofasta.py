import xml.etree.ElementTree as ET

def xml_to_fasta(xml_file, fasta_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(fasta_file, "w") as fasta:
        for seq in root.findall(".//sequence"):
            taxon_elem = seq.find("taxon")
            if taxon_elem is not None and "idref" in taxon_elem.attrib:
                taxon = taxon_elem.attrib["idref"]
            else:
                taxon = "Unknown_Taxon"  # Assign a default name if missing

            sequence = seq.text.strip() if seq.text else ""  # Handle empty sequences
            if sequence:
                fasta.write(f">{taxon}\n{sequence}\n")

# Example usage
#xml_to_fasta("input.xml", "output.fasta")


# Example usage
input = r"C:\Users\nurhu\Documents\raxml-ng_v1.2.0_linux_x86_64\input.xml"
xml_to_fasta(input, "output.fasta")
