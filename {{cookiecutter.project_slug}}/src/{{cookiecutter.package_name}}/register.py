from {{ cookiecutter.package_name }}.example import goal, rule, target_types
from {{ cookiecutter.package_name }}.target_types import ProtobufSourceTarget


def target_types():
    return (ProtobufSourceTarget,)


def rules():
    return (
        *goal.rules(),
        *rule.rules(),
    )
