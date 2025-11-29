# Use a modern, slim base image
FROM python:3.11-slim-bullseye 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir opentelemetry-distro opentelemetry-exporter-otlp \
    && opentelemetry-bootstrap -a install

# Copy application code
COPY . .

# Flask default port
EXPOSE 5000

# Set OpenTelemetry environment variables
ENV OTEL_SERVICE_NAME=your-service-name
ENV OTEL_TRACES_EXPORTER=console,otlp
ENV OTEL_METRICS_EXPORTER=console
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://jaeger:4318/v1/traces

# Run the application with OpenTelemetry instrumentation
CMD ["opentelemetry-instrument", "python", "app.py"]
