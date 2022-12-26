# cloud-storage

Library to access Cloud Storage using Python

## Installation

Install Python in your machine and execute the following:

```shell
python -m venv env
source ./env/bin/activate
pip install -e .
```

## Run

Authenticate with Google:

```shell
gcloud auth application-default login
```

Run example:

```shell
python cloud_storage/google.py
```
