import csv
import pandas as pd

class CsvServices():

    def __init__(self):
        pass

    def save_csv_file(obj_list,exportation_folder):
        
        filename = exportation_folder+'csv_data.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Author', 'Title', 'Keywords','Abstract','Year', 'Type Publication', 'DOI','Book Title/Journal'])
            
            for item in obj_list:
                writer.writerow([item.author, item.title, item.keywords,item.abstract,item.year, item.type_publication, item.doi, item.book_journal])

    def read_csv_file(path):
        
        df = pd.read_csv(path,
                  sep=';', encoding='utf-8', low_memory=False,)
        return df
