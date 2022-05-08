from heapq import merge
from os import sep
import pandas as pd
import json
import yaml
from read_impact import read_impact

def treat_dataframe(dict_list, cols, opt_filter, query_df):
    df_bibtex = pd.DataFrame(dict_list)
    df_bibtex.rename(columns = {"title": "Title"}, inplace = True)
    df_bibtex['journal'] = df_bibtex['journal'].str.upper()
    df_impacto = read_impact()
    merged_df = pd.merge(df_bibtex, df_impacto, how = 'inner', on = 'journal')
    merged_df.drop_duplicates(subset = ['Title', 'journal'])
    new_df = merged_df
    new_df['keywords'] = new_df['keywords'].str.replace(';',",")
    new_df['year'] = pd.to_numeric(new_df['year'], errors = 'coerce')
    new_df['SJR'] = pd.to_numeric(new_df['SJR'], errors = 'coerce')
    new_df['JIR'] = pd.to_numeric(new_df['JIR'], errors = 'coerce')
    if opt_filter == 'yes':
        new_df.query(query_df, engine = 'python', inplace = True)
        new_df = merged_df.filter(items = cols['cols_to_show'])
    return new_df

def to_xml(row):
    xml = ['<item>']
    for field in row.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
    xml.append('</item>')
    return '\n'.join(xml)

def df_to_json(merged_df, nm_arq):
    merged_df.to_json(nm_arq + '_from_df.json', orient='records')

def df_to_csv(merged_df, nm_arq):
    merged_df.to_csv(nm_arq + "_from_df.csv", sep = '|')

def df_to_yaml(merged_df, nm_arq):
    data=json.loads(merged_df.to_json(orient='records'))
    with open(nm_arq + '_from_df.yaml', 'w') as yml:
        yaml.dump(data, yml, allow_unicode=False)

def df_to_xml(merged_df, nm_arq):
    file = open(nm_arq + "_from_df.xml", "w", encoding='UTF-8') 
    file.write('\n'.join(merged_df.apply(to_xml, axis=1)),) 
    file.close()
