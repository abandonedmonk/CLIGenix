FROM python:3.11-slim

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /project

COPY requirements.txt /project/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY pyproject.toml /project/pyproject.toml
COPY README.md /project/README.md
COPY cligenix /project/cligenix

RUN pip install -e .

ENTRYPOINT ["cligenix"]

