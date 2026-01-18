FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask aiohttp

# Expose port
EXPOSE 9999

# Run the app
CMD ["python", "app.py"]
