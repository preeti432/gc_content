library(Biostrings)

# Read FASTA file
seq <- readDNAStringSet("gene.fna")

# Count G and C
gc <- letterFrequency(seq, letters = c("G", "C"))

# Calculate GC percentage
gc_percent <- sum(gc) / sum(width(seq)) * 100

# Display result
cat("GC Content:", round(gc_percent, 2), "%\n")
