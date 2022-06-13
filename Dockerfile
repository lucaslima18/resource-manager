# Importing python image
FROM python:3.8

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy actual dir to image
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install dependencies and create virtual environment
RUN python -m venv venv
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install django
RUN pip install djangorestframework
RUN pip install psycopg2-binary
RUN pip install drf-yasg
RUN . venv/bin/activate