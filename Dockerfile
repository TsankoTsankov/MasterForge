FROM python:3.10-slim

WORKDIR /app

# Install dependencies first (for caching speed)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Open the port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]