# Dealership Review Portal

This repository contains a Django-based dealership review portal with static and React frontend pages, authentication, dealer search, review posting, and sentiment analysis.

## Project Overview

- **Project Name:** Dealership Review Portal
- **Tech Stack:** Django, React, Bootstrap, MongoDB/Express (API), NLTK
- **Features:** User registration, login/logout, dealer browsing, dealer review posting, sentiment analysis, about/contact pages.

## Project Structure

- `server/` - Django backend, static frontend pages, API views, and data sources.
- `server/frontend/static/` - Static HTML pages used by Django routes.
- `server/frontend/src/` - React application components.
- `server/database/` - Express/MongoDB API server and seeded dealer/review data.

## Run Locally

From `server/`:

```bash
c:/Users/emman/Desktop/coder/.venv/Scripts/python.exe manage.py migrate --settings=djangoproj.settings
c:/Users/emman/Desktop/coder/.venv/Scripts/python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Important Pages

- `/about` - About Us page
- `/contact` - Contact Us page
- `/dealers` - Dealer listing page
- `/dealer/<id>` - Dealer details and reviews
- `/postreview/<id>` - Post review page
- `/login` - User login page
- `/register` - User registration page
