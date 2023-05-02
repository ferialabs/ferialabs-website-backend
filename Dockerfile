FROM tiangolo/uvicorn-gunicorn:python3.10
WORKDIR /app
USER root

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Files and Secrets
COPY ./ferialabs ./ferialabs
# Looking for b64 encoded secret environment variables
RUN --mount=type=secret,id=ENV_SECRETS cat /run/secrets/ENV_SECRETS | base64 -d >> ./.env
# Copy entrypoin file
COPY ./entrypoint.sh ./entrypoint.sh

# Create a dockeruser to own the app
RUN useradd -r dockeruser
RUN chown dockeruser: /app
USER dockeruser

ENV PYTHONPATH "${PYTHONPATH}:/app"
