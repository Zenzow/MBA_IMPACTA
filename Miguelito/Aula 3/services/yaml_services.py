from dis import show_code
from logging import exception
from mimetypes import init
import yaml

class YamlServices():

    def __init__(self):
        pass
    
    def import_yaml_exported():
        with open('project_files/exports/yaml_data.yaml', 'r') as file:
            yaml_config_file = yaml.safe_load(file)
        return yaml_config_file

    def get_path_from_yaml(yaml_file):
        bibtex_path = yaml_file['file_origen'][0]['folder']
        return bibtex_path

    def save_yaml_file(yaml_files,exportation_folder):
        with open(exportation_folder+'yaml_data.yaml', 'w') as outfile:
            outfile.write(yaml_files)

    def dict_to_yaml(obj_list):
        yaml_list=yaml.dump(obj_list,indent=3)
        return yaml_list

    def filter_validation(yaml_file):
        exportation_type=yaml_file['exportation_type'][0]['type']
        exportation_type_list=yaml_file['supported_exportation_types'][0]['supported_types']
        yaml_file['exportation_type'][0]['type']=YamlServices.exportation_type_validation(exportation_type,exportation_type_list)


        ano=yaml_file['filter_options'][0]['year']
        yaml_file['filter_options'][0]['year']=YamlServices.ano_validation(ano)

        equality_supported_list=yaml_file['supported_type_equality'][0]['supported_types']

        year_equality=yaml_file['filter_options'][0]['year_equality']
        yaml_file['filter_options'][0]['year_equality']=YamlServices.type_equality_validation(year_equality,equality_supported_list,'year_equality')
       
        jcr_value_equality=yaml_file['filter_options'][0]['jcr_value_equality']
        yaml_file['filter_options'][0]['jcr_value_equality']=YamlServices.type_equality_validation(jcr_value_equality,equality_supported_list,'jcr_value_equality')
       
        scimago_value_equality=yaml_file['filter_options'][0]['scimago_value_equality']
        yaml_file['filter_options'][0]['scimago_value_equality']=YamlServices.type_equality_validation(scimago_value_equality,equality_supported_list,'scimago_value_equality')

        jcr_value=yaml_file['filter_options'][0]['jcr_value']
        yaml_file['filter_options'][0]['jcr_value']=YamlServices.ranking_value_validation(jcr_value,'jcr_value')
       
        scimago_value=yaml_file['filter_options'][0]['scimago_value']
        yaml_file['filter_options'][0]['scimago_value']=YamlServices.ranking_value_validation(scimago_value,'scimago_value')

        type_publication=yaml_file['filter_options'][0]['type_publication']
        type_publication_list=yaml_file['supported_type_publication'][0]['supported_types']
        yaml_file['filter_options'][0]['type_publication']=YamlServices.type_publication_validation(type_publication,type_publication_list)

        print('Filters to be applied are:\n')
        
        for key,value in yaml_file['filter_options'][0].items():
        
           print(f'{key}: {value}')
        print()
        exportation_type=yaml_file['exportation_type'][0]['type']
        print(f'exportation type: {exportation_type}')
        print()

        return yaml_file

        
    def ano_validation(ano):
        if ano!='':
            try:
                ano=int(ano)
            except ValueError as error:
                print('Year value must be int type')
                ano=''
                print('Year filter will not be applied\n')
            except:
                print('Unexpected error related to year filter has occurred ')
                ano=''
                print('Year filter will not be applied\n')
        return ano

    def ranking_value_validation(value,type):
        if value!='':
            try:
                value=float(value)
            except ValueError as error:
                print(f'{type} value must be decimal type formated with "."')
                value=''
                print(f'{type} filter will not be applied\n')
            except:
                print(f'Unexpected error related to {type} filter has occurred ')
                value=''
                print(f'{type} filter will not be applied\n')
        
        return value

    def type_publication_validation(type_publication,list):

        if type_publication!='':
       
            try:
                list.index(type_publication)
            except ValueError as error:
                type_publication=''
                print(f'\ntype Publication is not permited, it should be one of these:{list}\ntype Pulication filter will not be applied\n')
                  
        return type_publication
      
    def type_equality_validation(equality,list,type):
       
        if equality!='':
            try:
                list.index(equality)
            except ValueError as error:
                print(f'\n{equality} is not permited, it should be one of these:{list}\n{type} applied will be "=="\n')
                equality='=='
                    
        return equality

    def exportation_type_validation(exportation_type,list):
        if exportation_type!='':
            try:
                list.index(exportation_type)
            except ValueError as error:
                print(f'\n{exportation_type} is not permited, it should be one of these:{list}\nExportation type applied will be "CSV"\n')
                exportation_type='csv'
                    
        return exportation_type



 
       
        
        
        


    






        


          

     
           
