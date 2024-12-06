import warnings

warnings.filterwarnings(
    "ignore", ".*obsolete", UserWarning, "google.protobuf.runtime_version"
)
