import read_dataset as helper
import datasets_pb2

with open('models/mnist.onnx', 'rb') as f:
    ds = datasets_pb2.Dataset()
    ds.ParseFromString(f.read())
    for it in helper.read_ds(ds):
        print(it)
