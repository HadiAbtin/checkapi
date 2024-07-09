ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD gunicorn --no-sendfile \
  --bind 0.0.0.0:8080 \
  --access-logfile - --error-logfile - \
  --workers 4 app:app
