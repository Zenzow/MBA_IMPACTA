import pymysql
import pandas as pd
import numpy as np

def python_sql(df):
    #cols = "', '".join([str(i) for i in df.columns.tolist()])
    con = pymysql.connect(host = 'localhost', db = 'teste_zenzo', user='root', password = '123456')
    cursor = con.cursor()
    df = df.replace(np.nan, 'empty')
    for i, row in df.iterrows():
        sql = """INSERT INTO tb_zenzo_python_de (author, title, keywords, year, type_publication,
            doi, abstract, journal, sjr, jir) values (""" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql, (tuple(row)))
        con.commit()
    # Create a new query that selects the entire contents of `employee`
    sql = "SELECT * FROM tb_zenzo_python_de"
    cursor.execute(sql)

    # Fetch all the records and use a for loop to print them one line at a time
    result = cursor.fetchall()
    for i in result:
        print(i)
    con.close()

if __name__ == '__main__':
    python_sql('a')
    cursor.execute("""create table if not exists tb_zenzo_python_de (
                    author varchar(100) null,
                    title varchar(200) null,
                    keywords varchar(300) null,
                    year smallint null,
                    type_publication varchar(50) null,
                    doi varchar(30) null,
                    abstract varchar(1000) null,
                    journal varchar(50) null
                    );""")
    comando = """sudo service mysql status
                 sudo service mysql start
                 sudo service mysql status
                 sudo mysql -p"""