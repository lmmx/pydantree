#!/bin/bash

curl -Ls https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

./bin/micromamba shell init -s bash -r ~/micromamba
# Python interpreter lives at /vercel/micromamba/bin/python
source ~/.bashrc

# activate the environment and install a new version of Python
micromamba activate
micromamba install python=3.12 -c conda-forge -y

# install the dependencies
python --version
python -m pip install pdm 'urllib3<2'
pdm install --no-default -dG docs -v
pdm run mkdocs
