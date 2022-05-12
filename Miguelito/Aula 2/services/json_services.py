class JsonServices():

    def __init__(self):
        pass

    def save_json_file(json_file,exportation_folder):
       with open(exportation_folder+'json_data.json', 'w') as outfile:
           outfile.write(json_file)