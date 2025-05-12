FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gettext \
    pylint \
    default-libmysqlclient-dev \
    build-essential \
    git \
    pkg-config \
    python3-dev \
    default-mysql-client \
    libmariadb-dev \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /vol/janeway/src

# Copy requirements first to leverage Docker cache
COPY requirements.txt dev-requirements.txt ../

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir mysqlclient && \
    pip install --no-cache-dir -r ../requirements.txt && \
    pip install --no-cache-dir -r ../dev-requirements.txt

# Copy the rest of the application
COPY . /vol/janeway/

# Copy settings file
RUN cp core/janeway_global_settings.py core/settings.py

# Expose port and set entrypoint
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
