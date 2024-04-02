import os
import collections
import glob

# Lista putanja do direktorija
directories = [
    "C:/*/Machine17/Croatian_Invoices_snippets",
    "C:/*/Machine17/French_Invoices_snippets",
    "C:/*/Machine17/Spanish_Invoices_snippets"
]

# Funkcija za čitanje prvog reda i izračunavanje frekvencije znakova
def calculate_frequencies(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        first_line = file.readline()
        return collections.Counter(first_line)

# Rječnik za spremanje ukupnih frekvencija
total_frequencies = collections.Counter()

# Prođi kroz sve putanje i datoteke
for directory in directories:
    for file_path in glob.glob(os.path.join(directory, '*.txt')):
        total_frequencies.update(calculate_frequencies(file_path))

# Sortiraj rezultate
sorted_frequencies = total_frequencies.most_common()

# Ispis rezultata
print("{:<10} {:<10}".format('Char', 'Freq'))
print("{:<10} {:<10}".format('-----', '--------'))

for char, freq in sorted_frequencies:
    print("{:<10} {:<10}".format(repr(char), freq))
