import pandas as pd

class Etl():
    def __init__(self):
      pass

    def sci_etl(sci):
      sci = sci.dropna(subset=['SJR'])
      sci2=sci.copy()
      sci2['SJR']=sci2['SJR'].str.replace(',', '.')
      sci2['SJR'] = sci2['SJR'].apply(lambda sjr: float(sjr))
      sci2=Etl.create_upper_title(sci2,'Title')
      sci2.rename(columns={'Title':'Title_SCI','SJR':'SCI_FACTOR'},inplace=True)
      sci2 = sci2[['Title_SCI', 'TITLE_UPPER', 'SCI_FACTOR']]
      return sci2
    
    
    def jcr_etl(jcs):
      jcs2=jcs.copy()
      jcs2=Etl.create_upper_title(jcs2,'Full Journal Title')
      jcs2 = jcs2[jcs2['Journal Impact Factor'] != 'Not Available']
      jcs2['Journal Impact Factor'] = jcs2['Journal Impact Factor'].apply(
          lambda x: float(x))
      jcs2.rename(columns={'Full Journal Title':'Title_JCS','Journal Impact Factor':'JCS_FACTOR'},inplace=True)
      jcs2 = jcs2[['Title_JCS', 'TITLE_UPPER', 'JCS_FACTOR']]
      return jcs2

    def merge_etl(sci,jcs,original_csv):

      # MERGING 
      merged=pd.merge(original_csv,sci,how='left',on='TITLE_UPPER')
      merged=pd.merge(merged,jcs,how='left',on='TITLE_UPPER')
      
      # ETL MERGED FILE 
      merged=merged[['Author', 'Title', 'Keywords', 'Abstract', 'Year', 'Type Publication',
       'DOI', 'Book Title/Journal', 'TITLE_UPPER', 'Title_SCI','Title_JCS' ,'SCI_FACTOR', 'JCS_FACTOR']]
      merged['SCI_FACTOR']=merged['SCI_FACTOR'].fillna(0)
      merged['JCS_FACTOR']=merged['JCS_FACTOR'].fillna(0)
      merged=merged.fillna('N/A')
      merged['DOI']=merged['DOI'].astype(str)
      return merged

    def create_upper_title(df,column_name):
      df['TITLE_UPPER'] = df[column_name].apply(lambda name: name.upper())
      return df

    



