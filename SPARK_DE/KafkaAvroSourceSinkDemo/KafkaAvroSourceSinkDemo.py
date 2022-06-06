from pyspark.sql import SparkSession
from pyspark.sql.avro.functions import to_avro, from_avro
from pyspark.sql.functions import from_json, col, expr, struct, to_json
from pyspark.sql.types import ArrayType, StructType, StructField, StringType, LongType, DoubleType, IntegerType

from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Multi Query Demo") \
        .master("local[3]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .getOrCreate()

    logger = Log4j(spark)

    kafka_source_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "invoice-items") \
        .option("startingOffsets", "earliest") \
        .load()

    avroSchema = open(r"C:\Users\GUSTAVO\Desktop\MBA_IMPACTA\Spark\Aula_Kafka_Spark\KafkaAvroSourceDemo\schema\invoice-items", mode='r').read()

    value_df = kafka_source_df.select(from_avro(col("value"), avroSchema).alias("value"))

    kafka_target_df = value_df.select(expr("value.InvoiceNumber as key"),
                                        to_avro(struct("value.CreatedTime")).alias("value"))

    invoice_writer_query = kafka_target_df \
        .writeStream \
        .queryName("Flattened Invoice Writer") \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("topic", "invoice-items") \
        .outputMode("append") \
        .option("checkpointLocation", "KafkaAvroSourceSinkDemo\chk-point-dir") \
        .start()

    logger.info("Start Writer Query")
    invoice_writer_query.awaitTermination()
