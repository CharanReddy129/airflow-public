FROM apache/airflow:3.0.2-python3.9
USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt