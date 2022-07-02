import sqlite3
import os
from pyspark.sql import SparkSession
import findspark
from pyspark.sql.functions import *
from pyspark import SparkContext
from pyspark.sql import SQLContext

def spark_sqlite(df_stream):
    sc = SparkContext.getOrCreate()
    sqlctx = SQLContext(sc)

    df_sqlite = sqlctx.read.format("jdbc").options(url ="jdbc:sqlite:banco.db", driver="org.sqlite.JDBC", dbtable="conta_corrente").load()

    df_sqlite.show()
    joined_df = df_stream.join(df_sqlite, df_stream.cd_cli == df_sqlite.cod_cliente, "inner")

    joined_df =  joined_df.drop("cod_cliente")

    joined_df_2 = joined_df.withColumn("regra", \
        when((joined_df.valor_operacao > joined_df.saldo_conta) & (joined_df.tipo_operacao == "Saque"), lit("Cheque especial")) \
                .when((joined_df.saldo_conta > 50000), lit("Elegivel a cartao Black")) \
                .otherwise(lit("N/A")) \
                ).show()
    return joined_df_2



if __name__ == "__main__":
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    #cria_tabela = "CREATE TABLE IF NOT EXISTS conta_corrente (cod_cliente int PRIMARY KEY,nome text, idade int, gerente text, conta int ,tip_conta text, score int)"
    cursor.execute("DROP TABLE TRANSACAO_ENR")
    cria_tabela = "CREATE TABLE IF NOT EXISTS TRANSACAO_ENR (cd_cli int, agencia int,valor_operacao int,tipo_operacao text,data_hora datetime,saldo_conta float,nome text,idade smallint,gerente text,conta int,tip_conta text,score smallint,decision text)"
    #cria_cliente = "INSERT INTO conta_corrente VALUES (1, 'Antonio Santos', 43, 'Geraldo Rodrigues', 3785, 'P', 15)"
    #cria_cliente2 = "INSERT INTO conta_corrente VALUES (2, 'Gabriela Antonina', 22, 'Geraldo Rodrigues', 3785, 'C', 90)"
    #cria_cliente3 = "INSERT INTO conta_corrente VALUES (3, 'Magna Silva', 25, 'Paulo P.', 3785, 'R', 99)"
    


    cursor.execute(cria_tabela)
    #cursor.execute(cria_cliente)
    #cursor.execute(cria_cliente2)
    #cursor.execute(cria_cliente3)
    connection.commit()

    v_sql = "select * from conta_corrente"
    cursor.execute(v_sql)
    resultado = cursor.fetchall()
    print(resultado)
    v_sql = "select * from transacao_enr"
    cursor.execute(v_sql)
    resultado = cursor.fetchall()
    print(resultado)
    connection.close()