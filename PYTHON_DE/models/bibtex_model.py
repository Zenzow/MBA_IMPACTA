class BibtexModel():

    def __init__(self, author, title, keywords, year, type_publication, doi, abstract, journal):
        self.author = author
        self.title = title
        self.keywords = keywords
        self.year = year
        self.type_publication = type_publication
        self.doi = doi
        self.abstract = abstract
        self.journal = journal

    def __repr__(self):
        return f'\n\n\nAUTHOR:{self.author}\nTITLE:{self.title}\nKEYWORDS:{self.keywords}\nYEAR:{self.year}\nTYPE PUBLICATION:{self.type_publication}\nDOI:{self.doi}\nABSTRACT:{self.abstract}\nJOURNAL:{self.journal})'

    def dump_json(self):
        return {"Valor": {'author': self.author,
                          'title': self.title,
                          'keywords': self.keywords,
                          'year': self.year,
                          'type_publication': self.type_publication,
                          'doi': self.doi,
                          'abstract': self.abstract,
                          'journal': self.journal
                          }}
