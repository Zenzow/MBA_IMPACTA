import yaml
import os
import glob
from bib_converter import bib_reader_writer

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
    nm_arq = formato_export.get("nome_do_arquivo")
    fmt = formato_export.get("formato_export")
    if fmt not in ["yaml", "json", "csv"]:
        print("Formato " + fmt + " não suportado!")
        exit()
    bib_reader_writer(files_to_process, nm_arq, fmt)
