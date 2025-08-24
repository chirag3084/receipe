# Recipe App 🍳

A Django-based web application for managing and sharing recipes.

## Features

- **Recipe Management**: Create, view, edit, and delete recipes
- **User Authentication**: Secure user registration and login system
- **Recipe Categories**: Organize recipes by categories
- **Search Functionality**: Find recipes quickly
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default) / PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/chirag3084/receipe.git
   cd receipe
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
receipe/
├── manage.py
├── requirements.txt
├── receipe/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── recipes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Usage

### Adding a Recipe

1. Log in to your account
2. Click on "Add Recipe"
3. Fill in the recipe details:
   - Title
   - Description
   - Ingredients
   - Instructions
   - Cooking time
   - Category
4. Save the recipe

### Searching Recipes

- Use the search bar to find recipes by name or ingredients
- Filter recipes by category
- Browse all recipes on the main page

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows PEP 8 style guidelines. Please ensure your code is properly formatted before submitting.

## Environment Variables

Create a `.env` file in the root directory for sensitive settings:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=your_database_url_here
```

## Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Create a Heroku app
3. Set environment variables
4. Deploy using Git

```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Chirag
- **GitHub**: [@chirag3084](https://github.com/chirag3084)
- **Repository**: [receipe](https://github.com/chirag3084/receipe)

## Acknowledgments

- Django documentation and community
- Bootstrap for responsive design
- Font Awesome for icons

---

⭐ If you found this project helpful, please give it a star!