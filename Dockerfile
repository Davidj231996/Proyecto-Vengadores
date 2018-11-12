FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 80
CMD ["python", "API_WEB.py"]
EXPOSE 80