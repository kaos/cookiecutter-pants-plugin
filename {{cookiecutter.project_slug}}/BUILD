python_distribution(
    name="dist",
    provides=python_artifact(
        name="{{ cookiecutter.project_slug }}",
        version="{{ cookiecutter.project_version }}",
    ),
    dependencies=["src/{{ cookiecutter.package_name }}"],
    entry_points={
        "pantsbuild.plugin": {
            "rules": "{{ cookiecutter.package_name }}.register:rules",
            "target_types": "{{ cookiecutter.package_name }}.register:target_types",
        }
    },
{%- if cookiecutter.twine_publish_repo %}
    repositories=["{{ cookiecutter.twine_publish_repo }}"],
{%- endif %}
    sdist=True,
    wheel=True,
)
