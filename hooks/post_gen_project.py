#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def parse_os_release(path=Path("/etc/os-release")):
    lines = path.read_text().splitlines()
    os_version = None
    os_id = None
    for line in lines:
        key, *values = line.split("=")
        value = "=".join(values).replace('"', "").replace("'", "")
        if key == "ID":
            os_id = value
        elif key == "VERSION_ID":
            os_version = value
    if not os_id or not os_version:
        raise ValueError(f"Expected to find both ID and VERSION_ID in {path}")
    return os_version, os_id


def create_venv(venv_name, python_version):
    if "VENV_HOME" not in os.environ:
        raise ValueError("ERROR: You must export VENV_HOME!")

    os_version, os_id = parse_os_release()
    venv_name = f"{venv_name}-py{python_version}-{os_id}{os_version}"
    python_path = Path(f"python{python_version}")

    venv_path = (Path(os.environ["VENV_HOME"]) / venv_name).absolute()
    if venv_path.exists():
        response = input(
            f"{str(venv_path)!r} already exists. Continue on, using the existing venv? [y]/n  "
        )
        if response and response.lower() != "y":
            raise ValueError("Bailing out")
        print(f"Using existing venv '{venv_path}'...")
    else:
        print(f"Creating '{venv_path}'...")
    subprocess.check_call([python_path, "-m", "venv", venv_path], text=True)
    venv_python = venv_path / "bin" / "python"
    print("Upgrading pip and build tools...")
    subprocess.check_call(
        [
            venv_python,
            "-m",
            "pip",
            "install",
            "-U",
            "pip",
            "setuptools",
            "build",
            "wheel",
            "flit",
        ],
        text=True,
    )
    subprocess.check_call(
        [venv_python, "-m", "pip", "install", "-e", "."],
        text=True,
    )
    print(
        f"Successfully created {venv_path}; activate it via\n"
        f"  $ source {venv_path}/bin/activate"
    )


def my_create_venv():
    try:
        create_venv(
            "{{ cookiecutter.project_slug }}", "{{ cookiecutter.python_version }}"
        )
    except ValueError as error:
        raise ValueError(
            "Failed to create venv {{ cookiecutter.project_slug }} {{ cookiecutter.python_version }}"
        ) from error


def git_init():
    subprocess.check_call(["git", "init"], text=True, cwd=PROJECT_DIRECTORY)
    subprocess.check_call(["pre-commit", "install"], text=True, cwd=PROJECT_DIRECTORY)
    subprocess.check_call(["git", "add", "-A"], text=True, cwd=PROJECT_DIRECTORY)
    subprocess.check_call(
        ["git", "commit", "-m", "Initial commit"], text=True, cwd=PROJECT_DIRECTORY
    )


def main():
    git_init()
    if "{{cookiecutter.create_venv}}".lower() == "y":
        my_create_venv()


if __name__ == "__main__":
    main()
