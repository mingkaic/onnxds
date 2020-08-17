load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

def protobuf_repository():
    git_repository(
        name = "com_google_protobuf",
        remote = "https://github.com/protocolbuffers/protobuf",
        tag = "v3.10.0",
    )
