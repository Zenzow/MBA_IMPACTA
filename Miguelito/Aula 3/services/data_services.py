from tkinter.tix import InputOnly


class DataServices():

    def __init__(self):
        pass

    def filter_values(values, df):

        if values['title'] != '':
            title = values['title']
            df = DataServices.filter_column_single_string(
                'Book Title/Journal', title, df)

        if values['keywords'] != ['']:
            keywords = values['keywords']
            df = DataServices.filter_column_list_string(
                'Keywords', keywords, df)

        if values['abstract'] != '':
            abstract = values['abstract']
            df = DataServices.filter_column_single_string(
                'Abstract', abstract, df)

        if values['year'] != '':
            year_equality = values['year_equality']
            year = int(values['year'])
            df = DataServices.filter_column_number(
                'Year', year_equality, year, df)

        if values['type_publication'] != '':
            type_publication = values['type_publication']
            df = DataServices.filter_column_single_string(
                'Type Publication', type_publication, df)

        if values['doi'] != '':
            abstract = values['doi']
            df = DataServices.filter_column_single_string(
                'DOI', abstract, df)

        if values['jcr_value'] != '':
            jcr_equality = values['jcr_value_equality']
            jcr = int(values['jcr_value'])
            df = DataServices.filter_column_number(
                'JCS_FACTOR', jcr_equality, jcr, df)

        if values['scimago_value'] != '':
            scimago_equality = values['scimago_value_equality']
            scimago = int(values['scimago_value'])
            df = DataServices.filter_column_number(
                'SCI_FACTOR', scimago_equality, scimago, df)

        return df

    def filter_column_single_string(column, string, df):
        df = DataServices.add_upper_column(column, df)
        string = string.upper()
        df = df[df[column+'_UPPER'].str.contains(string)]
        del df[column+'_UPPER']
        return df

    def filter_column_list_string(column, list_strings, df):
        df = DataServices.add_upper_column(column, df)
        list_strings = list(map(lambda x: x.upper(), list_strings))
        df = df[df[column+'_UPPER'].str.contains('|'.join(list_strings))]
        del df[column+'_UPPER']
        return df

    def filter_column_number(column, equality, number, df):
        expression = f"{column} {equality} {number}"
        df = df.query(expression)
        # df = df.query("`Year` >= 23000")
        return df

    def add_upper_column(column, df):
        df[column+'_UPPER'] = df[column].apply(lambda name: name.upper())
        return df
