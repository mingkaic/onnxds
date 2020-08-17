
bazel-bin/external/com_google_protobuf/protoc:
	bazel build @com_google_protobuf//:protoc

.PHONY: gen-proto
gen-proto: bazel-bin/external/com_google_protobuf/protoc
	./bazel-bin/external/com_google_protobuf/protoc --python_out=. -I . datasets.proto onnx/onnx.proto

.PHONY: generate_mnist
generate_mnist:
	bazel run //:tfgen_dataset -- --out /tmp/mnist.onnx --split TRAIN mnist
	mv /tmp/mnist.onnx models
