from pyspark.sql import SparkSession
from pyspark.sql.avro.functions import to_avro, from_avro
from pyspark.sql.functions import from_json, col, expr, struct, to_json
from sqlite_db import spark_sqlite


from lib.logger import Log4j

if __name__ == "__main__":
    def enriquecer(df_stream, batchID):
        if df_stream.count()>0:
            df_stream.show()
            df_enr = spark_sqlite(df_stream)
            print("Processado")
            return(df_enr)

    spark = SparkSession \
        .builder \
        .appName("spark_streaming") \
        .master("local[3]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .getOrCreate()

    logger = Log4j(spark)
    
    kafka_source_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "transacao_inicial_1") \
        .option("startingOffsets", "earliest") \
        .option("failOnDataLoss", "false") \
        .load()
    avroSchema = open(r"schema_transacao_entrada.avsc", mode='r').read()

    value_df = kafka_source_df.select(from_avro(col("value"), avroSchema).alias("value")).select("value.*")
    print(value_df)
    value_df.printSchema()
    #kafka_target_df = value_df.select(to_avro(struct("value")).alias("value"))
    
    transacao_final = value_df \
        .writeStream \
        .queryName("Exemplo Transacao") \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .foreachBatch(enriquecer) \
        .option("topic", "transacao_final") \
        .outputMode("append") \
        .option("checkpointLocation", "KafkaAvroSourceSink\chk-point-dir") \
        .start()
         
    logger.info("Start Writer Query")
    transacao_final.awaitTermination()
