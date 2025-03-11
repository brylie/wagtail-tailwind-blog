# Wagtail Tailwind Blog

A modern blog built with Wagtail CMS and styled with Tailwind CSS. Features a responsive design, dark mode support, and accessibility-first approach.

## Features

- 🎨 Tailwind CSS styling with dark mode support
- 📱 Fully responsive design
- ♿ Accessibility-first components
- 🚀 Fast development workflow
- 📝 Rich text editing with Wagtail
- 🌗 Dark mode support

## Prerequisites

- Python 3.8+
- Node.js 14+
- pip
- virtualenv (recommended)

## Setup

1. Create and activate a virtual environment:
```bash
cd app
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:
```bash
python manage.py tailwind install
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

## Development

You'll need two terminal windows to run the development server:

### Terminal 1 - Django/Wagtail Server
```bash
cd app
python manage.py runserver
```

### Terminal 2 - Tailwind CSS Watcher
```bash
cd app
python manage.py tailwind start
```

The site will be available at:
- Main site: http://localhost:8000
- Admin interface: http://localhost:8000/admin

## Project Structure

- `/app` - Main Django project directory
- `/app/blog` - Blog app with models and templates
- `/app/core` - Core functionality and base templates
- `/app/home` - Home page app

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
