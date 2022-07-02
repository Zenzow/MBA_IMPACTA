from kafka import KafkaProducer
import io
from avro.schema import Parse
from avro.io import DatumWriter, DatumReader, BinaryEncoder, BinaryDecoder

#iniciar o zookeeper no F:
#iniciar o kafka no F:/Kafka
#producer produz dados no tópico transacao_inicial


# Create a Kafka client ready to produce messages
bootstrap_servers = ['localhost:9092']
topicName = 'transacao_inicial_1'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Get the schema to use to serialize the message
schema = Parse(open('schema_transacao_entrada.avsc', "rb").read())

# serialize the message data using the schema
buf = io.BytesIO()
encoder = BinaryEncoder(buf)
writer = DatumWriter(writer_schema=schema)
#writer.write({"cd_cli": 1, "agencia": 7, "valor_operacao": 1010.11 , "tipo_operacao":"Saque","data_hora":"04/06/2022","saldo_conta":1000.00}, encoder)
writer.write({"cd_cli": 1, "agencia": 7, "valor_operacao": 1010.11 , "tipo_operacao":"Deposito","data_hora":"04/06/2022","saldo_conta":1000.00}, encoder)
#writer.write({"cd_cli": 2, "agencia": 7, "valor_operacao": 10000.00 , "tipo_operacao":"Deposito","data_hora":"04/06/2022","saldo_conta":100000.00}, encoder)
#writer.write({"cd_cli": 3, "agencia": 5, "valor_operacao": 100000.00 , "tipo_operacao":"Deposito","data_hora":"04/06/2022","saldo_conta":1000000.00}, encoder)
#writer.write({"agencia": 7, "valor_operacao": 10.00 , "tipo_operacao":"Saque","data_hora":"04/06/2022","saldo_conta":1000.00}, encoder)
buf.seek(0)
message_data = (buf.read())

# message key if needed
key = None

# headers if needed
headers = []

# Send the serialized message to the Kafka topic
producer.send(topicName,
              message_data,
              key,
              headers)
producer.flush()