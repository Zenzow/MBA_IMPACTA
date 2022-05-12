import yaml
import pandas as pd

class ImportationServices():
    def __init__(self):
        pass

    def import_yaml_config():
        with open('config.yaml', 'r') as file:
            yaml_config_file = yaml.safe_load(file)
        return yaml_config_file

    def read_csv_file(path):
        df = pd.read_csv(path,
                  sep=';', encoding='utf-8', low_memory=False,)
        return df
  