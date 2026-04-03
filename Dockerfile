# Root Dockerfile for Render when "Docker" is selected as the environment.
# Context: repository root. Copies the Django app from server/.

FROM python:3.11-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -c "import nltk; nltk.download('vader_lexicon')"

COPY server/ .

RUN python manage.py collectstatic --noinput

EXPOSE 10000

# Render injects PORT at runtime; migrate keeps SQLite schema current on fresh disks.
CMD sh -c "python manage.py migrate --noinput && exec gunicorn djangoproj.wsgi:application --bind 0.0.0.0:${PORT}"
