class FilterOptionsModel():

    def __init__(self, suported_type_publication, supported_type_equality, title, keywords, abstract, year_equality, year, type_publication, doi, jcr_value_equality, jcr_value, scimago_value_equality, scimago_value):
        self.suported_type_publication = suported_type_publication
        self.supported_type_equality = supported_type_equality
        self.title = title
        self.keywords = keywords
        self.abstract = abstract
        self.year_equality = year_equality
        self.year = year
        self.type_publication = type_publication
        self.doi = doi
        self.jcr_value_equality = jcr_value_equality
        self.jcr_value = jcr_value
        self.scimago_value_equality = scimago_value_equality
        self.scimago_value = scimago_value

    
    def validate_filters(self):
      self.year=FilterOptionsModel.year_validation(self.year)
      self.year_equality=FilterOptionsModel.type_equality_validation(self.year_equality,self.supported_type_equality,'year_equality')

      self.jcr_value=FilterOptionsModel.ranking_value_validation(self.jcr_value,'jcr_value')
      self.jcr_value_equality=FilterOptionsModel.type_equality_validation(self.jcr_value_equality,self.supported_type_equality,'jcr_value_equality')

      

    
    def type_equality_validation(equality,list,type):
       
        if equality!='':
            try:
                list.index(equality)
            except ValueError as error:
                equality='=='
                print(f'\n{equality} is not permited, it should be one of these:{list}\n{type} applied will be "=="\n')
                    
        return equality
        
    
    def year_validation(year):
        # if not isinstance(self.year,(int)):
        #     raise ValueError('Year needs to be numeric int type')

        if year != '':
            try:
                year = int(year)
            except ValueError as error:
                print('Year value must be int type')
                year = ''
                print('Year filter will not be applied\n')
            except:
                print('Unexpected error related to year filter has occurred ')
                year = ''
                print('Year filter will not be applied\n')
        return year
      
    
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


# supported_type_publication:
#   - supported_types: ['inproceedings','article','inbook','techreport','book','proceedings','incollection']

# supported_type_equality:
#   - supported_types: ['<=','<','==','>','>=','!=']

# filter_options:
#   - title: ''               # text value, '' for empty
#     keywords: ['']                           # text values, ex: ['BIG DATA', 'ANALISYS'], [''] for empty
#     abstract: ''                             # text value, '' for empty
#     year_equality: '=='                       # equality value in ['<=','<','==','>','>=','!=']
#     year: 'ldfkjsd'                             # int value, ex: 2019, '' for empty
#     type_publication: ''              # text value in ['inproceedings','article','inbook','techreport','book','proceedings','incollection'] or '' for none
#     doi: ''                                  # text value, '' for empty
#     jcr_value_equality: '>='                # equality value in ['<=','<','==','>','>=','!=']
#     jcr_value: ''                        # decimal value, ex: 343.12, '' for empty
#     scimago_value_equality: '>='            # equality value in ['<=','<','==','>','>=','!=']
#     scimago_value: ''
