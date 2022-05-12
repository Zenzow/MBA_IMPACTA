import csv

class CsvServices():

    def __init__(self):
        pass

    def save_csv_file(obj_list,exportation_folder):
        
        filename = exportation_folder+'csv_data.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Author', 'Title', 'Keywords','Year', 'Type Pulication', 'DOI'])
            
            for item in obj_list:
                writer.writerow([item.author, item.title, item.keywords,item.year, item.type_publication, item.doi])
