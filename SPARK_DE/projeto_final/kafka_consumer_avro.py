import io
import avro.schema
import avro.io
from kafka import KafkaConsumer



# To consume messages
CONSUMER = KafkaConsumer('transacao_final',
                         group_id='group1',
                         bootstrap_servers=['localhost:9092'])

SCHEMA_PATH = "schema_transacao_entrada.avsc"
SCHEMA = avro.schema.parse(open(SCHEMA_PATH).read())
print("aqui")
for msg in CONSUMER:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(SCHEMA)
    user1 = reader.read(decoder)
    print("aqui2")
    print(user1)