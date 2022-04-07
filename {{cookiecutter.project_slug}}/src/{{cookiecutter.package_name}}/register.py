from {{ cookiecutter.package_name }}.example import goal, rule, target_types


def target_types():
    return (
        target_types.ProtobufSourceTarget,
    )


def rules():
    return (
        *goal.rules(),
        *rule.rules(),
    )
