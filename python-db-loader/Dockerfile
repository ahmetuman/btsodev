FROM python:3.9-slim
WORKDIR /app
COPY loader.py .
RUN pip install requests
CMD ["python", "loader.py"]
