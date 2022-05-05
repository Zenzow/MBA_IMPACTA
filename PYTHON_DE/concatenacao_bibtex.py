import sys
import glob
from datetime import datetime
import yaml
from bib_converter import bib_reader_writer


def read_config():
    arquivos = {}
    export = {}
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    arquivos = config.get('SOURCES')
    export = config.get('DADOS_EXPORT')
    return arquivos, export


def list_bib_files(dict_bibs,anomesdia):
    dict_bibtex_bibfiles = {}
    for bib_files, dados in dict_bibs.items():
        list_of_bib_files = []
        for files in glob.glob(dados.get("directory") + dados.get("namestring") + "*" + anomesdia + '*' +'.bib'):
            list_of_bib_files.append(files)
        dict_bibtex_bibfiles[bib_files] = list_of_bib_files
    return dict_bibtex_bibfiles


if __name__ == "__main__":
    if len(sys.argv) > 1:
        anomesdia = sys.argv[1]
        try:
            datetime(int(str(anomesdia)[0:4]),
                     int(str(anomesdia)[4:6]),
                     int(str(anomesdia)[6:8]))
        except Exception as e:
            raise ValueError("Data informada é inválida! Informe-a no formato YYYYMMDD: {}".format(e))
        #print(anomesdia)
    else:
        anomesdia = ''
    bibs, formato_export = read_config()
    files_to_process = list_bib_files(bibs,anomesdia)
    nm_arq = formato_export.get("nome_do_arquivo")
    fmt = formato_export.get("formato_export")
    if fmt not in ["yaml", "json", "csv"]:
        print("Formato " + fmt + " não suportado!")
        exit()
    bib_reader_writer(files_to_process, nm_arq, fmt)
