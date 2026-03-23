# Portfolio Website

A professional portfolio website built with Django and Bootstrap 5. Allows showcasing projects and technical skills, and includes a contact form managed through the admin panel.

## Tech Stack

**Backend:**
- Python 3.11
- Django 4.2.7
- MySQL 8.0 / SQLite (fallback)
- Gunicorn

**Frontend:**
- Bootstrap 5.3.2
- Particles.js 2.0.0
- Swiper 11
- Font Awesome 6.4.2

**DevOps:**
- Docker & Docker Compose

## Features

- Hero section with animated particles (Particles.js) and typing effect
- About section with description and statistics
- Technology grid with icons
- Project carousel (Swiper) with links to GitHub and live demo
- Contact form that saves messages to the database
- Django admin panel for managing all site content
- Responsive design

## Getting Started

### With Docker Compose (recommended)

```bash
# Copy the example environment file
cp .env.example .env

# Start the containers
docker-compose up --build
```

The site will be available at `http://localhost:8000`.

### Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start the development server
python manage.py runserver
```

## Environment Variables

Configure the `.env` file based on `.env.example`:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Debug mode (`True`/`False`) |
| `ALLOWED_HOSTS` | Allowed hosts (comma-separated) |
| `DB_ENGINE` | Database engine (`sqlite3` or `mysql`) |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |

## Admin Panel

After starting the server, create a superuser:

```bash
python manage.py createsuperuser
```

The admin panel is available at `http://localhost:8000/admin/`. It allows managing:
- The About section
- Technology list
- Projects and their details
- Contact form messages
