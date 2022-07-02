from kafka import KafkaProducer
import io
from avro.schema import Parse
from avro.io import DatumWriter, DatumReader, BinaryEncoder, BinaryDecoder

# Create a Kafka client ready to produce messages
bootstrap_servers = ['localhost:9092']
topicName = 'sample'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Get the schema to use to serialize the message
schema = Parse(open('schema_transacao.avsc', "rb").read())

# serialize the message data using the schema
buf = io.BytesIO()
encoder = BinaryEncoder(buf)
writer = DatumWriter(writer_schema=schema)
# writer.write({"name": "Ben", "favorite_number": 7, "favorite_color": "red"}, encoder)
writer.write({"cd_cli": 1, "agencia": 7, "valor_operacao": 10.00 , "tipo_operacao":"Deposito","data_hora":"04/06/2022","saldo_conta":1010.00}, encoder)
# writer.write({"name": "Alyssa", "favorite_number": 256}, encoder)
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