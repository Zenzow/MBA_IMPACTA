import json
import yaml
from dict2xml import dict2xml

class ConvertionServices():
    
    def __init__(self):
        pass

    def convert_csv_to_dict_list(csv):
        dict_file = csv.to_dict(orient='records')
        return dict_file

    def convert_dict_to_json(dict):
        json_file = json.dumps(dict)
        return json_file

    def convert_dict_to_yaml(dict):
        yaml_file=yaml.dump(dict)
        return yaml_file

    def convert_dict_xml(dict):
        xml_file=dict2xml(dict)
        return xml_file






