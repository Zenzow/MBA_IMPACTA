import pandas as pd

def read_impact():
    df_jcr = pd.read_csv("jcr_scimago/jcs_2020.csv", sep = ";",
                        usecols = ["Full Journal Title", "Journal Impact Factor"],
                        low_memory = False)
    df_jcr.rename(columns = {"Full Journal Title": "Title", "Journal Impact Factor" : "JIR"}, inplace = True)
    df_jcr['Title'] = df_jcr['Title'].str.upper()
    df_scim = pd.read_csv("jcr_scimago/scimagojr_2020.csv", sep = ";", usecols = ["Title", "SJR"],
                        low_memory = False)
    df_scim['Title'] = df_scim['Title'].str.upper()
    merged_df = pd.merge(df_scim, df_jcr, how = 'left', on = 'Title')
    return merged_df
