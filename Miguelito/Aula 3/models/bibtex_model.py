import json
import yaml

class BibtexModel():

    def __init__(self, author, title, keywords,abstract, year, type_publication, doi,book_journal):
        self.author = author
        self.title = title
        self.keywords = keywords
        self.abstract=abstract

        self.year = year
        self.type_publication = type_publication
        self.doi = doi
        self.book_journal = book_journal

    def __repr__(self):
        return f'\n\n\nAUTHOR: {self.author}\nTITLE: {self.title}\nKEYWORDS: {self.keywords}\nABSTRACT: {self.abstract}\nYEAR: {self.year}\nTYPE PUBLICATION: {self.type_publication}\nDOI: {self.doi}\nBOOK/JOURNAL: {self.book_journal})'

    
    def dump_json(self):
        return {"Valor": {'author': self.author,
                          'title': self.title,
                          'keywords': self.keywords,
                          'abstract':self.abstract,
                          'year': self.year,
                          'type_publication': self.type_publication,
                          'doi': self.doi,
                          'book_journal': self.book_journal,

                          }}

    
    def bibtex_to_object(bib_list):
        obj_list = []
        for valor in bib_list:
            for valor2 in valor.entries:
                obj_list.append(BibtexModel(valor2.get('author', 'empty'), valor2.get('title', 'empty'), valor2.get('keywords', 'empty'),valor2.get('abstract', 'empty'), valor2.get('year', 'empty'), valor2.get('ENTRYTYPE', 'empty'), valor2.get('doi', 'empty'), valor2.get('booktitle', valor2.get('journal','empty'))))
        return obj_list
    
    
    def object_to_json(obj_list):
        json_obj = json.dumps([o.dump_json() for o in obj_list], indent=3)
        return json_obj

    

    def object_to_dict(obj_list):
        dict_list=[]
        for valor in obj_list:
            dict_list.append({'author':valor.author,'title':valor.title,'keywords':valor.keywords,'abstract':valor.abstract,'year':valor.year,'type_publication':valor.type_publication,'doi':valor.doi,'book_title':valor.book_journal})
        return dict_list

    


