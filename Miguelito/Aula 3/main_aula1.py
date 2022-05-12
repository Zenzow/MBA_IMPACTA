from models.bibtex_model import BibtexModel
from services.bibtex_services import BibtexServices
from services.csv_services import CsvServices
from services.json_services import JsonServices
from services.yaml_services import YamlServices


print('\n\tINÍCIO\n')


# Importando YAML
yaml_file = YamlServices.import_yaml_config()


# Lista de tipos de exportação suportadas
supported_types = yaml_file['supported_exportation_types'][0]['supported_types']


# Verificando o tipo de exportação que consta no YAML
exportation_type = yaml_file['exportation_type'][0]['type']


# Pegando caminho dos arquivos Bibtex que estão no arquivo config.yaml
bibtex_files_path = YamlServices.get_path_from_yaml(yaml_file)


# Pegando caminho para exportação dos arquivo que consta no YAML
exportation_folder = yaml_file['file_destination'][0]['folder']


# Pegando Lista de arquivos Bibtex
file_list = BibtexServices.get_file_list(bibtex_files_path)


# Importando Bibtex
bib_list = BibtexServices.read_bibtex_from_folder(file_list)


# Convertendo o BIBTEX em OBJETO
obj_list = BibtexModel.bibtex_to_object(bib_list)


if exportation_type == 'json':
    # Convertendo Objeto para Json
    json_file = BibtexModel.object_to_json(obj_list)
    # print(json_obj)

    # Salvando Json
    JsonServices.save_json_file(json_file, exportation_folder)
    print('Arquivo Json salvo com sucesso\n')


elif exportation_type == 'csv':
    # Salvando CSV
    CsvServices.save_csv_file(obj_list, exportation_folder)
    print('Arquivo CSV salvo com sucesso\n')


elif exportation_type == 'yaml':
    # Convertendo objeto para Dict
    dict_list = BibtexModel.object_to_dict(obj_list)

    # Convertento Dict para Yaml
    yaml_files = YamlServices.dict_to_yaml(dict_list)

    # Salvando YAML
    YamlServices.save_yaml_file(yaml_files, exportation_folder)
    print('Arquivo YAML salvo com sucesso\n')


else:
    print('Invalid exportation type\n')


print('\t FIM\n')
