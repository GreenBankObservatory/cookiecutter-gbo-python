import os
import re
import sys
import subprocess


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def check_module_name():
    module_name = "{{ cookiecutter.project_slug}}"
    if not re.match(MODULE_REGEX, module_name):
        print(
            f"ERROR: The project slug ({module_name}) is not a valid Python module name. "
            "Please do not use a - and use _ instead"
        )

        # Exit to cancel project
        sys.exit(1)


def check_deps():
    if "{{ cookiecutter.create_venv}}".lower() == "y" and "VENV_HOME" not in os.environ:
        raise ValueError(
            "ERROR: You must export VENV_HOME, or set 'create_venv=false'!"
        )
    try:
        subprocess.check_output(["which", "git"], text=True)
    except subprocess.CalledProcessError:
        raise ValueError("git must be installed and available on PATH")
    try:
        subprocess.check_output(["which", "pre-commit"], text=True)
    except subprocess.CalledProcessError:
        raise ValueError("pre-commit must be installed and available on PATH")


if __name__ == "__main__":
    check_module_name()
    check_deps()
