def reversed(self):
    s = self
    return s[::-1]

def comple(self):
    DNA = self.upper()
    
    components = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
        }

    complement_dna = ""

    for char in range(len(DNA)):
        complement_dna += components[DNA[char]]

    return complement_dna

def validateSeq(self):

    nucleotides = ["A", "T", "G", "C"]

    seq = self.upper()
    for nuc in seq:
        if nuc not in nucleotides:
            return False
    return seq