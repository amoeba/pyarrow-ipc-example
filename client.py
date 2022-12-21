import pyarrow as pa
from pyarrow.lib import IpcWriteOptions
import requests
import numpy as np

ENDPOINT_URI = "http://localhost:5000/batch"


def generate_example_batch(length=1_000):
    data = [pa.array(np.random.rand(length)), pa.array(np.repeat("a" * 64, length))]

    return pa.record_batch(data, names=["x", "y"])

def generate_example_batches(n=5):
    return [generate_example_batch() for i in range(n)]

def batches_to_bytes(batches, compression=None):
    sink = pa.BufferOutputStream()

    with pa.ipc.new_stream(
        sink, batches[0].schema, options=IpcWriteOptions(compression=compression)
    ) as writer:
        [writer.write_batch(batch) for batch in batches]

    return sink.getvalue()


def run():
    batches = generate_example_batches()
    bytes = batches_to_bytes(batches, compression=None)

    req = requests.post(ENDPOINT_URI, data=bytes)

    print(req.text)


if __name__ == "__main__":
    run()
