
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "file_processor.py"]  # Use "api_consumer.py" for the API consumer service.
