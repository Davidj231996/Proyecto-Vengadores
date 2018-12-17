FROM python:latest

WORKDIR /

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD web: gunicorn api_web:app --log-file -