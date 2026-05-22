FROM python:3.11-slim

WORKDIR /app

# Install only the absolute essentials for building C-based python kits
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "Valuation_search.py", "--server.port=8501", "--server.address=0.0.0.0"]