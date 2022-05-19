from ast import keyword
from sqlite3 import connect
import json
from urllib.error import HTTPError
from xplore.xploreapi import XPLORE
from models.bibtex_model import BibtexModel
from treat_df import treat_dataframe, df_to_csv, df_to_json, df_to_xml, df_to_yaml
import yaml

def connect_api(query_string):
    try:
        data_json = {}
        with open("key.txt", "r") as file:
            key = file.read()
        query = XPLORE(key)
        query.queryText(query_string)
        data = query.callAPI()
        data_json = json.loads(data)
        #print(type(data_json['articles']))
        data_dict = data_json['articles']
        with open('json_data.json', 'w') as outfile:
            json.dump(data_dict, outfile)
        #print(data_json)
        return data_dict

    except HTTPError as http_err:
        print(f'HTTP error ocurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error ocurred. Please check!')

def api_to_model(articles):
    obj_model = []
    dict_list = []
    for valor in articles:
        authors_list = ''
        keywords = ''
        for authors in valor.get('authors').get('authors'):
            if valor.get('authors').get('authors').index(authors) != (len(valor.get('authors').get('authors')) - 1):
                sep = ', '
            else:
                sep = ''
            authors_list = authors_list + authors.get('full_name') + sep
        for sessions in valor.get('index_terms'):
            for terms in valor.get('index_terms').get(sessions):
                for term in valor.get('index_terms').get(sessions).get(terms):
                   keywords = keywords + term + ', '
        keywords = keywords.strip()
        obj_model.append(BibtexModel(authors_list, valor.get('title', 'empty'), keywords, valor.get('publication_year', 'empty'), '', valor.get('doi', 'empty'), valor.get('abstract', 'empty'), valor.get('publication_title', 'empty')))
    for valor in obj_model:
        dict_list.append({'author':valor.author,
                          'title':valor.title,
                          'keywords':valor.keywords,
                          'year':valor.year,
                          'type_publication':valor.type_publication,
                          'doi':valor.doi,
                          'abstract':valor.abstract,
                          'journal':valor.journal})
    return dict_list
