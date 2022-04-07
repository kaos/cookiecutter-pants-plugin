from pants.engine.rules import collect_rules, rule


@rule
async def int_to_str(i: int) -> str:
    return str(i)


def rules():
    return collect_rules()
