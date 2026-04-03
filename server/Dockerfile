# Use this when Render "Root Directory" is set to `server` (Docker build context = server/).

FROM python:3.11-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -c "import nltk; nltk.download('vader_lexicon')"

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 10000

CMD sh -c "python manage.py migrate --noinput && exec gunicorn djangoproj.wsgi:application --bind 0.0.0.0:${PORT}"
