from pants.engine.target import COMMON_TARGET_FIELDS, Dependencies, SingleSourceField, Target


class ProtobufSourceField(SingleSourceField):
    expected_file_extensions = (".proto",)


class ProtobufSourceTarget(Target):
    alias = "protobuf_source"
    help = "A single Protobuf file."
    core_fields = (*COMMON_TARGET_FIELDS, Dependencies, ProtobufSourceField)
