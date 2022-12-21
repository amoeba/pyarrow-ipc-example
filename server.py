from flask import Flask, request
import pyarrow as pa

app = Flask(__name__)


@app.post("/batch")
def batch():
    data = request.get_data()

    with pa.ipc.open_stream(data) as reader:
        schema = reader.schema
        batches = [b for b in reader]

    return f"Done. Received {len(batches)} batch(es) with schema:\n\n{schema}"
