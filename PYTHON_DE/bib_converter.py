import json
import csv
import yaml
import bibtexparser
from models.bibtex_model import BibtexModel

def bib_reader(dict_of_files):
    list_output = []
    dict_list = []
    for bib_files, list_of_files in dict_of_files.items():
        for file in list_of_files:
            with open(file) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            for valor in bib_database.entries:
                if 'journal' in valor:
                    journal = valor.get('journal')
                elif 'booktitle' in valor:
                    journal = valor.get('booktitle')
                list_output.append(BibtexModel(valor.get('author', 'empty'), valor.get('title', 'empty'), valor.get(
                    'keywords', 'empty'), valor.get('year', 'empty'), valor.get('ENTRYTYPE', 'empty'), 
                    valor.get('doi', 'empty'), valor.get('abstract', 'empty'), journal))
    for valor in list_output:
        dict_list.append({'author':valor.author,
                          'title':valor.title,
                          'keywords':valor.keywords,
                          'year':valor.year,
                          'type_publication':valor.type_publication,
                          'doi':valor.doi,
                          'abstract':valor.abstract,
                          'journal':valor.journal})
    json_obj = json.dumps([o.dump_json() for o in list_output], indent=3)
    return json_obj, dict_list, list_output


def bib_writer(nome_do_arquivo,formato_do_arquivo, json_obj, dict_list, list_output):
    if formato_do_arquivo == "all":
        bib2json(json_obj, nome_do_arquivo)
        bib2yaml(dict_list, nome_do_arquivo)
        bib2csv(list_output, nome_do_arquivo)
    elif formato_do_arquivo == "json":
        bib2json(json_obj, nome_do_arquivo)
    elif formato_do_arquivo == "yaml":
        bib2yaml(dict_list, nome_do_arquivo)
    elif formato_do_arquivo == "csv":
        bib2csv(list_output, nome_do_arquivo)

def bib2json(json_obj,nome_do_arquivo):
    with open(nome_do_arquivo + '.json', 'w') as outfile:
        outfile.write(json_obj)

def bib2yaml(dict_list, nome_do_arquivo):
    #print(sys.argv[1])
    yaml_data = yaml.dump(dict_list, indent=3)
    with open(nome_do_arquivo + '.yaml', 'w') as y:
        y.write(yaml_data)

def bib2csv(list_output, nome_do_arquivo):
    with open(nome_do_arquivo + ".csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Author', 'Title', 'Keywords',
                        'Year', 'Type Pulication', 'DOI'])
        for item in list_output:
            writer.writerow([item.author, item.title, item.keywords,
                            item.year, item.type_publication, item.doi])
