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
