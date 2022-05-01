import bibtexparser
import json
import yaml
from models.bibtex_model import BibtexModel

def bib2json(dict_of_files, nome_do_arquivo):
    list_output = []
    for bib_files, list_of_files in dict_of_files.items():
        for file in list_of_files:
            with open(file) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            for valor in bib_database.entries:
                list_output.append(BibtexModel(valor.get('author', 'empty'), valor.get('title', 'empty'), valor.get(
                    'keywords', 'empty'), valor.get('year', 'empty'), valor.get('ENTRYTYPE', 'empty'), valor.get('doi', 'empty')))

            json_obj = json.dumps([o.dump_json() for o in list_output], indent=3)

    with open(nome_do_arquivo + '.json', 'w') as outfile:
        outfile.write(json_obj)

    
    yaml_data = yaml.safe_load(json_obj)
    converted_yaml_data = yaml.dump(yaml_data)
    print(converted_yaml_data)
    with open(nome_do_arquivo + '.yaml', 'w') as y:
        y.write(converted_yaml_data)
