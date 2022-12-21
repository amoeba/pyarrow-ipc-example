# pyarrow-example_compressed-batches-over-http

An example showing how to send compressed RecordBatches over HTTP with PyArrow.

## Pre-requisities

- Python
- Python packages
    - pyarrow
    - requests
    - numpy
    - Flask

# Running

To run the server (receiving end):

```sh
flask --app server run
```

(In another shell) To run the client (and send record batches):

```sh
python client.py
```
