import bibtexparser
import csv
from models.bibtex_model import BibtexModel

def bib2csv(dict_of_files, nome_do_arquivo):
    list_output = []
    for bib_files, list_of_files in dict_of_files.items():
        for file in list_of_files:
            with open(file) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            for valor in bib_database.entries:
                list_output.append(BibtexModel(valor.get('author', 'empty'), valor.get('title', 'empty'), valor.get(
                    'keywords', 'empty'), valor.get('year', 'empty'), valor.get('ENTRYTYPE', 'empty'), valor.get('doi', 'empty')))


    with open(nome_do_arquivo + ".csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(['Author', 'Title', 'Keywords',
                        'Year', 'Type Pulication', 'DOI'])
        for item in list_output:
            writer.writerow([item.author, item.title, item.keywords,
                            item.year, item.type_publication, item.doi])
