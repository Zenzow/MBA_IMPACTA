import os
import bibtexparser

class BibtexServices():
    def __init__(self):
        pass

    def get_file_list(path):
        file_list = os.listdir(path)
        file_list = list(
            map(lambda x: "project_files/imports/bibtex_files/"+x, file_list))
        return file_list

    def read_bibtex_from_folder(file_list):
        bib_list = []

        # Criando lista de arquivos Bibtex
        for valor in file_list:
            with open(valor) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)
                bib_list.append(bib_database)

        return bib_list
