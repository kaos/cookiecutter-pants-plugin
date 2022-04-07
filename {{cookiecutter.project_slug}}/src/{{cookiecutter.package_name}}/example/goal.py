from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.rules import collect_rules, goal_rule


class HelloWorldSubsystem(GoalSubsystem):
    name = "hello-world"
    help = "An example goal."


class HelloWorld(Goal):
    subsystem_cls = HelloWorldSubsystem


@goal_rule
async def hello_world() -> HelloWorld:
    return HelloWorld(exit_code=1)


def rules():
    return collect_rules()
