from mimetypes import init
import yaml

class YamlServices():

    def __init__(self):
        pass

    def import_yaml_config():
        with open('config.yaml', 'r') as file:
            yaml_config_file = yaml.safe_load(file)
        return yaml_config_file
    
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
     
           
