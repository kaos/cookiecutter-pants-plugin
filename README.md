# Pantsbuild plugin cookie cutter template

This is a template to setup a new Pants plugin repository.


## Pre-requisities

This template requires `cookiecutter 2.x`, but as of this writing the latest released version to
PyPi is `1.7.3`. There is a temporary fork in place until the maintenance issues for the
cookiecutter project is hopefully resolved, so to install a drop-in replacement for the official
version:

    pip install ansys-cookiecutter

For more background:

 * https://github.com/cookiecutter/cookiecutter/issues/1636
 * https://github.com/pyansys/ansys-templates/pull/36


## Usage

To apply this template, simply run:

    cookiecutter gh:kaos/cookiecutter-pants-plugin
