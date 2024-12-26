import os

# Define the project structure
project_structure = {
    "directories": [
        "flask_app/",
        "flask_app/app/",
        "flask_app/app/routes/",
        "flask_app/app/models/",
        "flask_app/app/services/",
        "flask_app/app/templates/",
        "flask_app/app/static/",
        "flask_app/app/static/css/",
        "flask_app/app/static/js/",
        "flask_app/app/static/images/",
        "flask_app/tests/",
        "flask_app/migrations/",
    ],
    "files": {
        "flask_app/app/__init__.py": """\
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.routes import main
        app.register_blueprint(main.bp)

    return app
""",
        "flask_app/app/routes/__init__.py": "",
        "flask_app/app/routes/main.py": """\
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')
""",
        "flask_app/app/models/__init__.py": "",
        "flask_app/app/services/__init__.py": "",
        "flask_app/app/templates/base.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
""",
        "flask_app/app/templates/home.html": """\
{% extends 'base.html' %}

{% block content %}
<h1>Welcome to Flask App</h1>
{% endblock %}
""",
        "flask_app/app/static/css/styles.css": "",
        "flask_app/app/config.py": """\
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
        "flask_app/tests/__init__.py": "",
        "flask_app/tests/test_routes.py": """\
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
""",
        "flask_app/run.py": """\
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
""",
        "flask_app/requirements.txt": """\
flask
flask-sqlalchemy
flask-migrate
pytest
""",
        "flask_app/.gitignore": """\
.env
__pycache__/
*.pyc
instance/
*.sqlite3
migrations/
""",
        "flask_app/.env": """\
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///app.db
""",
    },
}


def create_project_structure():
    # Create directories
    for directory in project_structure["directories"]:
        os.makedirs(directory, exist_ok=True)

    # Create files
    for filepath, content in project_structure["files"].items():
        # Ensure the parent directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            file.write(content)


if __name__ == "__main__":
    create_project_structure()
    print("Flask project structure created successfully!")
