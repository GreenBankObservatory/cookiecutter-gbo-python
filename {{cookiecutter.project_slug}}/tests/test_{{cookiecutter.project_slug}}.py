#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import subprocess


def test_cli():
    """Sample pytest test function with the pytest fixture as an argument."""
    subprocess.check_call("{{ cookiecutter.project_slug }}")
