# Submission Checklist

This repository now contains the files required for the capstone grading submission.

## Files created for grading tasks

- `README.md` — Project name and description details.
- `django_server` — Terminal output showing the Django server running.
- `About.html` — Updated About Us page with correct CSS links, team details, and images.
- `Contact.html` — Updated Contact Us page with correct CSS links, active contact navigation, and image.
- `server/frontend/src/components/Register/Register.jsx` — React sign-up page with five input fields and Register button.
- `loginuser` — cURL command and login output.
- `logoutuser` — cURL command and logout output for a logged-in session.
- `getdealerreviews` — cURL command and output for dealer review retrieval.
- `getalldealers` — cURL command and output for retrieving all dealers.
- `getdealerbyid` — cURL command and output for retrieving dealer details by ID.
- `getdealersbyState` — cURL command and output for retrieving dealers in Kansas.
- `getallcarmakes` — cURL command and output for retrieving car makes and models.
- `analyzereview` — cURL command and output for sentiment analysis of "Fantastic services".
- `CICD` — Workflow step names and successful Django check output.
- `.github/workflows/cicd.yml` — GitHub Actions workflow definition.
- `deploymentURL` — Placeholder for the public deployment URL.

## Notes

- A Django superuser `root` was created for admin access.
- Screenshot files are not generated automatically and must be captured manually:
  - `admin_login.png`
  - `admin_logout.png`
  - `get_dealers.png`
  - `get_dealers_loggedin.png`
  - `dealersbystate.png`
  - `dealer_id_reviews.png`
  - `dealership_review_submission.png`
  - `added_review.png`
  - `deployed_landingpage.png`
  - `deployed_loggedin.png`
  - `deployed_dealer_detail.png`
  - `deployed_add_review.png`

## Running the app

From the `server/` directory:

```bash
c:/Users/emman/Desktop/coder/.venv/Scripts/python.exe manage.py migrate --settings=djangoproj.settings
c:/Users/emman/Desktop/coder/.venv/Scripts/python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.
