import yaml
import os
import glob
from bib2yaml import bib2yaml
from bib2json import bib2json
from bib2csv import bib2csv

def read_config():
    arquivos = {}
    export = {}
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    arquivos = config.get('SOURCES')
    export = config.get('DADOS_EXPORT')
    return arquivos, export


def list_bib_files(dict_bibs):
    dict_bibtex_bibfiles = {}
    for bib_files, dados in dict_bibs.items():
        list_of_bib_files = []
        for files in glob.glob(dados.get("directory") + dados.get("namestring") + "*"):
            list_of_bib_files.append(files)
        dict_bibtex_bibfiles[bib_files] = list_of_bib_files
    return dict_bibtex_bibfiles


if __name__ == "__main__":
    bibs, formato_export = read_config()
    files_to_process = list_bib_files(bibs)
    if formato_export.get("formato_export") == "yaml":
        bib2yaml(files_to_process,formato_export.get("nome_do_arquivo"))
    elif formato_export.get("formato_export") == "json":
        bib2json(files_to_process,formato_export.get("nome_do_arquivo"))
    elif formato_export.get("formato_export") == "csv":
        bib2csv(files_to_process,formato_export.get("nome_do_arquivo"))