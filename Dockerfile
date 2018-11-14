FROM python:latest

WORKDIR /

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn -b 0.0.0.0:80 API_WEB:app