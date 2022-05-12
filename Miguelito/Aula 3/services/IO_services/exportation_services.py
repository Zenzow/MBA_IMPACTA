class ExportationServices():
    def __init__(self):
        pass

    def export_csv(csv_file,exportation_folder):
        csv_file.to_csv(exportation_folder+'csv_data.csv')

    def export_json(json_file,exportation_folder):
        with open(exportation_folder+'json_data.json', 'w') as outfile:
            outfile.write(json_file)

    def export_yaml(yaml_files,exportation_folder):
        with open(exportation_folder+'yaml_data.yaml', 'w') as outfile:
            outfile.write(yaml_files)

    def export_xml(xml_files,exportation_folder):
        with open(exportation_folder+'xml_data.xml', 'w',encoding='utf-8') as outfile:
            outfile.write(xml_files)
