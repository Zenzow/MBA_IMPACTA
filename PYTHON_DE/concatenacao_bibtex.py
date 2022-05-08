import sys
import glob
from datetime import datetime
import yaml
from bib_converter import bib_reader, bib_writer
from treat_df import treat_dataframe, df_to_csv, df_to_json, df_to_xml, df_to_yaml


def read_config():
    arquivos = {}
    export = {}
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    arquivos = config.get('SOURCES')
    export = config.get('DADOS_EXPORT')
    filter = config.get('FILTERS')
    return arquivos, export, filter


def list_bib_files(dict_bibs,anomesdia):
    dict_bibtex_bibfiles = {}
    for bib_files, dados in dict_bibs.items():
        list_of_bib_files = []
        for files in glob.glob(dados.get("directory") + dados.get("namestring") + "*" + anomesdia + '*' +'.bib'):
            list_of_bib_files.append(files)
        dict_bibtex_bibfiles[bib_files] = list_of_bib_files
    return dict_bibtex_bibfiles

def valida_configs(fmt, filter):
    if fmt not in ["yaml", "json", "csv", "xml", "all"]:
        print("Formato " + fmt + " não suportado!")
        exit()
    for col in filter:
        if col not in ['Title', 'keywords', 'abstract', 'year', 'type_publication', 'doi', 'JIR', 'SJR']:
            print("Coluna " + col + " inválida para filtragem!")
            exit()
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

    return anomesdia


if __name__ == "__main__":
    bibs, formato_export, filter = read_config()
    nm_arq = formato_export.get("nome_do_arquivo")
    fmt = formato_export.get("formato_export")
    anomesdia = valida_configs(fmt, filter['cols_to_show'])
    files_to_process = list_bib_files(bibs,anomesdia)
    json_obj, dict_yaml, list_csv = bib_reader(files_to_process)
    merged_df = treat_dataframe(dict_yaml, filter)
    if fmt == 'all':
        df_to_yaml(merged_df, nm_arq)
        df_to_json(merged_df, nm_arq)
        df_to_csv(merged_df, nm_arq)
        df_to_xml(merged_df, nm_arq)
    elif fmt == 'json':
        df_to_json(merged_df, nm_arq)
    elif fmt == 'csv':
        df_to_csv(merged_df, nm_arq)
    elif fmt == 'yaml':
        df_to_csv(merged_df, nm_arq)
    elif fmt == 'xml':
        df_to_xml(merged_df, nm_arq)
    bib_writer(nm_arq, fmt, json_obj, dict_yaml, list_csv)
