FROM python:3.9-slim

WORKDIR /code

# Install PostgreSQL client and netcat
RUN apt-get update && apt-get install -y libpq-dev gcc netcat

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# Debugging step to verify netcat installation
RUN which nc

EXPOSE 8000

COPY entrypoint.sh /code/
ENTRYPOINT ["/code/entrypoint.sh"]
