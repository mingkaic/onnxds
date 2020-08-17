load("//third_party:repos/onnx.bzl", "onnx_repository")
load("//third_party:repos/protobuf.bzl", "protobuf_repository")

def dependencies(excludes = []):
    ignores = native.existing_rules().keys() + excludes

    if "com_github_onnx_onnx" not in ignores:
        onnx_repository()

    if "com_google_protobuf" not in ignores:
        protobuf_repository()
