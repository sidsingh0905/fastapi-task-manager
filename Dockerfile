# # Image for local
# # Use official Python image
# FROM python:3.12-slim

# # Set working directory
# WORKDIR /code

# # Copy and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the code
# COPY . .

# # Expose port
# EXPOSE 8000

# # Run FastAPI app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



# Image for production
FROM python:3.12-slim

ARG APP_USER=appuser
RUN groupadd -r $APP_USER && useradd -r -g $APP_USER -m $APP_USER

WORKDIR /app

COPY requirements.txt .
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev build-essential \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get remove -y gcc build-essential \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

COPY . .
RUN chown -R $APP_USER:$APP_USER /app
USER $APP_USER

ENV PORT=8000
CMD ["sh", "-c", "gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT}"]

