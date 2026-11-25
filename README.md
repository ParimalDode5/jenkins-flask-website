# DevOps Demo Website 

A small Flask website for demonstrating GitHub and Jenkins Freestyle CI integration.

## Requirements

- Python 3.12 or newer
- Git

## Run locally on Ubuntu

```bash
sudo apt update
sudo apt install python3-venv -y
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```
 
Open <http://127.0.0.1:5000>.

## Run automated tests

In another terminal (or after stopping the server):

```bash
source .venv/bin/activate
python -m unittest discover -v
```

The tests check the homepage, `/health`, and `/about` endpoints.

## Jenkins Freestyle build commands

Configure the Jenkins job to check out this GitHub repository, then add an **Execute shell** build step:

```bash
set -eu
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m py_compile app.py test_app.py
python -m unittest discover -v
zip -r website-build.zip app.py requirements.txt templates static README.md
```

In **Post-build Actions**, select **Archive the artifacts** and use:

```text
website-build.zip
```

For the practical's automatic build demonstration, configure **Poll SCM** with:

```text
H/2 * * * *
```

This checks the configured SCM repository approximately every two minutes. Jenkins needs `python3-venv`, Git, and network access to install dependencies.
