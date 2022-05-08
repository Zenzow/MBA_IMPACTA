from operator import contains
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

def valida_configs(fmt, filter_col, filter_active):
    if fmt not in ["yaml", "json", "csv", "xml", "all"]:
        print("Formato " + fmt + " não suportado!")
        exit()
    for col in filter_col:
        if col not in ['author', 'Title', 'keywords', 'abstract', 'year', 'type_publication', 'doi', 'JIR', 'SJR', 'journal']:
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
    if filter_active in ['yes', 'no']:
        opt_filter = filter_active
    else:
        print("Opção de filtro não reconhecida. Seguindo sem filtro.")
        opt_filter = 'no'

    return anomesdia, opt_filter

def creating_filter(vl_to_filter):
    filtros = {}
    query_string = ''
    conector = ''
    for chave, value in vl_to_filter.items():
        #print(chave, value)
        if value['cond'] is not None and value['text'] is not None:
            filtros[chave] = value
    print(filtros)
    for col, valor in filtros.items():
        if col != list(filtros.keys())[-1]:
            conector = valor['cond']
        if col in ['Title', 'keywords', 'abstract', 'type_publication', 'doi']:
            query_string = query_string + col + '.str.contains("' + valor['text'] + '") ' + conector + ' '
        if col in ['year', 'JIR', 'SJR']:
            query_string = query_string + col + ' ' + valor['tipo_comp'] + ' ' + str(valor['text']) + ' ' + conector + ' ' 
        conector = ''
    return(query_string)
    

if __name__ == "__main__":
    bibs, formato_export, filter = read_config()
    vl_filter = filter['values_to_filter']
    query_string = creating_filter(vl_filter)
    nm_arq = formato_export.get("nome_do_arquivo")
    fmt = formato_export.get("formato_export")
    anomesdia, opt_filter = valida_configs(fmt, filter['cols_to_show'], filter['active'])
    files_to_process = list_bib_files(bibs,anomesdia)
    json_obj, dict_yaml, list_csv = bib_reader(files_to_process)
    merged_df = treat_dataframe(dict_yaml, filter, opt_filter, query_string)
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
