import yaml
import os
import glob
from bib2yaml import bib2yaml


def read_config():
    arquivos = {}
    export = {}
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    print(config)
    arquivos = config.get('SOURCES')
    export = config.get('DADOS_EXPORT')
    return arquivos, export


def list_bib_files(dict_bibs):
    dict_bibtex_bibfiles = {}
    for bib_files, dados in dict_bibs.items():
        list_of_bib_files = []
        for files in glob.glob(dados.get("directory") + dados.get("namestring") + "*.bib"):
            list_of_bib_files.append(files)
        dict_bibtex_bibfiles[bib_files] = list_of_bib_files
    print(dict_bibtex_bibfiles)
    return dict_bibtex_bibfiles


if __name__ == "__main__":
    bibs, formato_export = read_config()
    files_to_process = list_bib_files(bibs)
    if formato_export.get("formato_export") == "yaml":
        bib2yaml(files_to_process)