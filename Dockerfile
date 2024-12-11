# syntax=docker/dockerfile:1
FROM python:3.12.3-alpine

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /flasky

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy the source code into the container.
COPY flasky/* .

# Run the application.
ENTRYPOINT ["python", "-m"]
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]