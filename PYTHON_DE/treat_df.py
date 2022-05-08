import pandas as pd
import json
import yaml
from read_impact import read_impact

def treat_dataframe(dict_list, cols):
    df_bibtex = pd.DataFrame(dict_list)
    df_bibtex.rename(columns = {"title": "Title"}, inplace = True)
    df_bibtex['Title'] = df_bibtex['Title'].str.upper()
    df_impacto = read_impact()
    merged_df = pd.merge(df_bibtex, df_impacto, how = 'left', on = 'Title')
    merged_df.drop_duplicates(subset = ['Title'])
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
    merged_df.to_csv(nm_arq + "_from_df.csv")

def df_to_yaml(merged_df, nm_arq):
    data=json.loads(merged_df.to_json(orient='records'))
    with open(nm_arq + '_from_df.yaml', 'w') as yml:
        yaml.dump(data, yml, allow_unicode=False)

def df_to_xml(merged_df, nm_arq):
    file = open(nm_arq + "_from_df.xml", "w", encoding='UTF-8') 
    file.write('\n'.join(merged_df.apply(to_xml, axis=1)),) 
    file.close()


