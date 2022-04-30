from tkinter.ttk import Separator
import bibtexparser
import pandas as pd

with open('./arquivos_bibtex/ieee.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

df = pd.DataFrame(bib_db.entries)
df.to_csv("teste.csv", index = False, sep = "|")