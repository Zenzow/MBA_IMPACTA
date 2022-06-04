import io
import avro.schema
import avro.io
from kafka import KafkaConsumer

# To consume messages
CONSUMER = KafkaConsumer('sample',
                         group_id='group1',
                         bootstrap_servers=['localhost:9092'])

SCHEMA_PATH = "schema_transacao.avsc"
SCHEMA = avro.schema.parse(open(SCHEMA_PATH).read())

for msg in CONSUMER:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(SCHEMA)
    user1 = reader.read(decoder)
    print(user1)