FROM python:3.10.6

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /app/
ENV DJANGO_SETTINGS_MODULE main.settings
ENV DJANGO_APP=main

EXPOSE 8000
CMD poetry run manage.py runserver
