from Bio import SeqIO

# Read FASTA file
record = SeqIO.read("gene.fna", "fasta")

# Get DNA sequence
sequence = str(record.seq).upper()

# Count nucleotides
a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

# Calculate GC content
gc_content = (g + c) / len(sequence) * 100

# Display results
print("Gene:", record.id)
print("Sequence Length:", len(sequence))
print("Adenine (A):", a)
print("Thymine (T):", t)
print("Guanine (G):", g)
print("Cytosine (C):", c)
print("GC Content: {:.2f}%".format(gc_content))
