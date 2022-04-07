# See https://www.pantsbuild.org/docs/rules-api-testing for more testing how-to's.

from pants.testutil.rule_runner import run_rule_with_mocks

from {{ cookiecutter.package_name }}.example.rule import int_to_str


def test_int_to_str() -> None:
    result: str = run_rule_with_mocks(int_to_str, rule_args=[42], mock_gets=[])
    assert result == "42"
